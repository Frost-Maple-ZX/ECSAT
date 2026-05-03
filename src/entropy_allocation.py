import numpy as np
import threading
from collections import deque
from typing import Dict, List, Tuple, Optional


class EntropyManager:
    """
    Entropy-based situation assessment for multi-agent spatiotemporal allocation.
    Implements spatial entropy H_s, temporal entropy H_t ,
    and communication entropy H_c  as defined in ECSAT.
    """

    NUM_DIRECTION_SECTORS = 8
    MAX_SPATIAL_ENTROPY = np.log2(NUM_DIRECTION_SECTORS)   # 3.0 bits

    NUM_VELOCITY_STATES = 4
    MAX_TEMPORAL_ENTROPY = np.log2(NUM_VELOCITY_STATES)    # 2.0 bits

    NUM_COMM_BINS = 4
    MAX_COMM_ENTROPY = np.log2(NUM_COMM_BINS)              # 2.0 bits

    DEFAULT_VELOCITY_THRESHOLDS = [0.1, 0.5, 1.5]         # m/s, for ground robots

    MAX_HISTORY_LENGTH = 1000
    VELOCITY_BUFFER_SIZE = 500
    COMM_BUFFER_SIZE = 500

    def __init__(self,
                 alpha: float = 1.0,
                 beta: float = 0.15,
                 gamma: float = 0.05,
                 delta: float = 0.02,
                 velocity_thresholds: Optional[List[float]] = None,
                 adaptive_thresholds: bool = True,
                 comm_bins: Optional[List[float]] = None):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta

        self.velocity_thresholds = velocity_thresholds
        self.adaptive_thresholds = adaptive_thresholds
        self._velocity_buffer = deque(maxlen=self.VELOCITY_BUFFER_SIZE)

        self.comm_bins = comm_bins
        self._comm_buffer = deque(maxlen=self.COMM_BUFFER_SIZE)
        self._comm_bins_learned = False

        self.spatial_volumes: Dict[int, deque] = {}
        self.velocity_profiles: Dict[int, deque] = {}
        self.renewal_times: Dict[Tuple[int, int], List[float]] = {}
        self.entropy_history: Dict[int, Dict[str, deque]] = {}

        self._direction_vectors = self._init_direction_vectors()
        self._lock = threading.RLock()

    def _init_direction_vectors(self) -> np.ndarray:
        angles = np.linspace(0, 2 * np.pi, self.NUM_DIRECTION_SECTORS, endpoint=False)
        return np.array([[np.cos(a), np.sin(a)] for a in angles])

    @staticmethod
    def _shannon_entropy(probabilities: np.ndarray) -> float:
        # H = -sum p_i * log2(p_i)
        p = probabilities[probabilities > 0]
        return -np.sum(p * np.log2(p)) if len(p) > 0 else 0.0

    def compute_spatial_entropy(self,
                                agent_id: int,
                                half_spaces_over_time: List[Tuple[float, dict]],
                                neighbor_positions: Optional[List[np.ndarray]] = None) -> float:
        """
        Compute spatial entropy H_s .
        Neighbor direction is approximated by -a, since a points into agent i's
        feasible half-space and the neighbor lies on the exterior side.
        """
        with self._lock:
            if not half_spaces_over_time:
                return 0.0

            sector_counts = np.zeros(self.NUM_DIRECTION_SECTORS)
            volumes = []

            for idx, (t, half_space) in enumerate(half_spaces_over_time):
                a = np.array(half_space['a']).flatten()
                b = half_space['b']
                current_pos = np.array(half_space.get('current_pos', [0, 0])).flatten()

                a = a[:2] if len(a) >= 2 else np.array([a[0], 0]) if len(a) == 1 else np.array([1, 0])
                current_pos = current_pos[:2] if len(current_pos) >= 2 else np.array([current_pos[0], 0]) if len(current_pos) == 1 else np.array([0, 0])

                distance_to_boundary = np.dot(a, current_pos) - b
                volumes.append(max(float(distance_to_boundary), 0.01))

                norm_a = np.linalg.norm(a)
                if norm_a > 1e-6:
                    if neighbor_positions is not None and idx < len(neighbor_positions):
                        neighbor_pos = np.array(neighbor_positions[idx]).flatten()[:2]
                        delta = neighbor_pos - current_pos
                        norm_delta = np.linalg.norm(delta)
                        neighbor_direction = delta / norm_delta if norm_delta > 1e-6 else -a / norm_a
                    else:
                        neighbor_direction = -a / norm_a

                    angle = np.arctan2(neighbor_direction[1], neighbor_direction[0])
                    if angle < 0:
                        angle += 2 * np.pi
                    sector_idx = int(angle / (2 * np.pi / self.NUM_DIRECTION_SECTORS)) % self.NUM_DIRECTION_SECTORS
                    sector_counts[sector_idx] += 1

            if agent_id not in self.spatial_volumes:
                self.spatial_volumes[agent_id] = deque(maxlen=self.MAX_HISTORY_LENGTH)
            self.spatial_volumes[agent_id].append(np.array(volumes))

            total = np.sum(sector_counts)
            if total < 1e-8:
                return 0.0

            probabilities = sector_counts / total
            H_spatial = self._shannon_entropy(probabilities)
            self._record_entropy(agent_id, 'spatial', H_spatial)
            return H_spatial

    def _get_velocity_thresholds(self, speeds: np.ndarray) -> List[float]:
        """
        Adaptive threshold update via quartiles .
        Falls back to DEFAULT_VELOCITY_THRESHOLDS when buffer is insufficient.
        """
        if self.velocity_thresholds is not None:
            return self.velocity_thresholds
        if not self.adaptive_thresholds:
            return self.DEFAULT_VELOCITY_THRESHOLDS

        self._velocity_buffer.extend(speeds.tolist())
        if len(self._velocity_buffer) < 50:
            return self.DEFAULT_VELOCITY_THRESHOLDS

        all_speeds = np.array(self._velocity_buffer)
        q25, q50, q75 = np.percentile(all_speeds, [25, 50, 75])

        q25 = max(q25, 0.01)
        if q50 <= q25: q50 = q25 * 2
        if q75 <= q50: q75 = q50 * 2

        return [q25, q50, q75]

    def compute_goal_entropy(self, agent_id: int, trajectory: dict) -> float:
        """Compute temporal entropy H_t ."""
        with self._lock:
            x = np.array(trajectory.get('x', []))
            y = np.array(trajectory.get('y', []))

            if len(x) < 2:
                return 0.0

            vx, vy = np.diff(x), np.diff(y)
            speeds = np.sqrt(vx ** 2 + vy ** 2)

            if agent_id not in self.velocity_profiles:
                self.velocity_profiles[agent_id] = deque(maxlen=self.MAX_HISTORY_LENGTH)
            self.velocity_profiles[agent_id].append(speeds)

            if len(speeds) == 0:
                return 0.0

            thresholds = self._get_velocity_thresholds(speeds)
            state_counts = np.zeros(self.NUM_VELOCITY_STATES)
            for v in speeds:
                if v < thresholds[0]:       state_counts[0] += 1
                elif v < thresholds[1]:     state_counts[1] += 1
                elif v < thresholds[2]:     state_counts[2] += 1
                else:                       state_counts[3] += 1

            probabilities = state_counts / len(speeds)
            H_temporal = self._shannon_entropy(probabilities)
            self._record_entropy(agent_id, 'temporal', H_temporal)
            return H_temporal

    def compute_communication_entropy(self,
                                      agent_pairs_renewal_times: Dict[Tuple[int, int], List[float]]) -> float:
        """
        Compute communication entropy H_c .
        Bins are learned from data and fixed once sufficient samples are collected.
        """
        with self._lock:
            all_intervals = []
            for pair, times in agent_pairs_renewal_times.items():
                if len(times) > 1:
                    intervals = np.diff(times)
                    all_intervals.extend(intervals)
                    self.renewal_times[pair] = times

            if len(all_intervals) == 0:
                return 0.0

            all_intervals = np.array(all_intervals)

            if self.comm_bins is None:
                self._comm_buffer.extend(all_intervals.tolist())
                if not self._comm_bins_learned and len(self._comm_buffer) >= 100:
                    all_hist = np.array(self._comm_buffer)
                    q25, q50, q75 = np.percentile(all_hist, [25, 50, 75])
                    self.comm_bins = [float(q25), float(q50), float(q75)]
                    self._comm_bins_learned = True

            bins = self.comm_bins if self.comm_bins is not None else np.percentile(all_intervals, [25, 50, 75]).tolist()

            bin_counts = np.zeros(self.NUM_COMM_BINS)
            for interval in all_intervals:
                if interval < bins[0]:      bin_counts[0] += 1
                elif interval < bins[1]:    bin_counts[1] += 1
                elif interval < bins[2]:    bin_counts[2] += 1
                else:                       bin_counts[3] += 1

            probabilities = bin_counts / len(all_intervals)
            return self._shannon_entropy(probabilities)

    def _record_entropy(self, agent_id: int, entropy_type: str, value: float):
        if agent_id not in self.entropy_history:
            self.entropy_history[agent_id] = {
                'spatial': deque(maxlen=self.MAX_HISTORY_LENGTH),
                'temporal': deque(maxlen=self.MAX_HISTORY_LENGTH),
                'communication': deque(maxlen=self.MAX_HISTORY_LENGTH)
            }
        self.entropy_history[agent_id][entropy_type].append(value)

    def compute_congestion_index(self, agent_id: int,
                                 half_spaces_over_time: List[Tuple[float, dict]]) -> float:
        with self._lock:
            volumes = []
            for t, half_space in half_spaces_over_time:
                a = np.array(half_space['a'])
                b = half_space['b']
                current_pos = np.array(half_space.get('current_pos', [0, 0]))
                distance_to_boundary = np.dot(a, current_pos) - b
                volumes.append(max(distance_to_boundary, 0.01))

            if not volumes:
                return 0.0

            volumes = np.array(volumes)
            if agent_id not in self.spatial_volumes:
                self.spatial_volumes[agent_id] = deque(maxlen=self.MAX_HISTORY_LENGTH)
            self.spatial_volumes[agent_id].append(volumes)
            return 1.0 / (np.min(volumes) + 0.1)

    def compute_smoothness_index(self, agent_id: int, trajectory: dict) -> float:
        with self._lock:
            x = np.array(trajectory.get('x', []))
            y = np.array(trajectory.get('y', []))

            if len(x) < 3:
                return 0.0

            vx, vy = np.diff(x), np.diff(y)
            speeds = np.maximum(np.sqrt(vx ** 2 + vy ** 2), 1e-3)
            accelerations = np.diff(speeds)

            if agent_id not in self.velocity_profiles:
                self.velocity_profiles[agent_id] = deque(maxlen=self.MAX_HISTORY_LENGTH)
            self.velocity_profiles[agent_id].append(speeds)
            return float(np.sum(accelerations ** 2))

    def compute_balance_index(self, volumes: np.ndarray) -> float:
        if len(volumes) == 0:
            return 0.0
        return np.std(volumes) / (np.mean(volumes) + 1e-8)

    def compute_sync_index(self, agent_pairs_renewal_times: Dict[Tuple[int, int], List[float]]) -> float:
        all_intervals = []
        for pair, times in agent_pairs_renewal_times.items():
            if len(times) > 1:
                all_intervals.extend(np.diff(times))
        if not all_intervals:
            return 0.0
        all_intervals = np.array(all_intervals)
        return np.std(all_intervals) / (np.mean(all_intervals) + 1e-8)

    def evaluate_allocation_quality(self, agent_id: int,
                                    half_spaces: List[Tuple[float, dict]],
                                    trajectory: dict,
                                    neighbor_positions: Optional[List[np.ndarray]] = None) -> dict:
        """
        Evaluate allocation quality combining entropy cost and
        physical constraint indices. Returns decision advice and strategy.
        """
        with self._lock:
            spatial_entropy = self.compute_spatial_entropy(agent_id, half_spaces, neighbor_positions)
            temporal_entropy = self.compute_goal_entropy(agent_id, trajectory)

            volumes = self.spatial_volumes[agent_id][-1] if agent_id in self.spatial_volumes and self.spatial_volumes[agent_id] else np.array([1.0])

            congestion = self.compute_congestion_index(agent_id, half_spaces)
            smoothness = self.compute_smoothness_index(agent_id, trajectory)
            balance = self.compute_balance_index(volumes)

            normalized_spatial = spatial_entropy / self.MAX_SPATIAL_ENTROPY
            normalized_temporal = temporal_entropy / self.MAX_TEMPORAL_ENTROPY
            entropy_cost = self.beta * normalized_spatial + self.gamma * normalized_temporal
            physical_cost = self.beta * congestion + self.gamma * smoothness + self.delta * balance
            total_cost = self.alpha * entropy_cost + (1 - self.alpha) * physical_cost

            bottleneck_idx = int(np.argmin(volumes)) if len(volumes) > 0 else 0
            decision_advice, risk_level, strategy = self._generate_decision_advice(spatial_entropy, temporal_entropy, congestion)

            return {
                'spatial_entropy': spatial_entropy,
                'temporal_entropy': temporal_entropy,
                'entropy_cost': entropy_cost,
                'congestion': congestion,
                'smoothness': smoothness,
                'balance': balance,
                'total_cost': total_cost,
                'bottleneck_time_idx': bottleneck_idx,
                'min_clearance': float(np.min(volumes)) if len(volumes) > 0 else 0.0,
                'volumes': volumes,
                'decision_advice': decision_advice,
                'risk_level': risk_level,
                'recommended_strategy': strategy
            }

    def _generate_decision_advice(self, spatial_entropy: float,
                                  temporal_entropy: float,
                                  congestion: float) -> Tuple[str, str, str]:
        risk_level = 'low'
        strategy = 'normal'
        advices = []

        if spatial_entropy > 2.5:
            advices.append("high H_s: constrained from all directions")
            risk_level = 'high'
            strategy = 'conservative'
        elif spatial_entropy > 1.5:
            advices.append("medium H_s: multi-directional constraints")
            risk_level = 'medium' if risk_level == 'low' else risk_level
        elif 0 < spatial_entropy < 0.5:
            advices.append("low H_s: free direction available")
            strategy = 'aggressive' if risk_level == 'low' else strategy

        if temporal_entropy > 1.5:
            advices.append("high H_t: unstable velocity profile")
            risk_level = 'high'
            strategy = 'conservative'
        elif temporal_entropy < 0.3:
            advices.append("low H_t: stable velocity")

        if congestion > 5.0:
            advices.append("critical congestion: replanning required")
            risk_level = 'high'
            strategy = 'emergency'
        elif congestion > 2.0:
            advices.append("high congestion: increase clearance")

        decision_advice = " | ".join(advices) if advices else "nominal"
        return decision_advice, risk_level, strategy

    def get_adaptive_weights(self, agent_id: int, num_neighbors: int,
                             distance_to_goal: float) -> Tuple[float, float, float]:
        """Adaptive weight scaling ."""
        beta_adaptive = self.beta * (1 + 0.1 * num_neighbors)
        gamma_adaptive = self.gamma * 2.0 if distance_to_goal < 1.0 else self.gamma
        delta_adaptive = self.delta * (1 + 0.05 * num_neighbors)
        return beta_adaptive, gamma_adaptive, delta_adaptive

    def optimize_allocation(self, agent_i, agent_j,
                            current_allocation: List[Tuple[float, dict]],
                            trajectory_i: dict,
                            trajectory_j: dict) -> List[Tuple[float, dict]]:
        """Entropy-guided boundary adjustment ."""
        with self._lock:
            half_spaces = self._extract_half_spaces(current_allocation, agent_i)
            quality = self.evaluate_allocation_quality(
                agent_i.index if hasattr(agent_i, 'index') else 0,
                half_spaces, trajectory_i
            )

            if quality['spatial_entropy'] < 2.0 and quality['temporal_entropy'] < 1.3 and quality['congestion'] < 2.0:
                return current_allocation

            volumes = quality['volumes']
            bottleneck_idx = quality['bottleneck_time_idx']
            entropy_factor = (quality['spatial_entropy'] / self.MAX_SPATIAL_ENTROPY +
                              quality['temporal_entropy'] / self.MAX_TEMPORAL_ENTROPY) / 2

            adjusted_allocation = []
            for k, (t, half_space) in enumerate(current_allocation):
                a = half_space['a']
                b = half_space['b']
                if k == bottleneck_idx or (k > 0 and abs(k - bottleneck_idx) <= 1):
                    base_adjustment = 0.1 * self.beta * (1.0 / (volumes[k] + 0.1))
                    entropy_adjustment = 0.05 * entropy_factor
                    b_adjusted = b - (base_adjustment + entropy_adjustment)
                else:
                    b_adjusted = b
                adjusted_allocation.append((t, {'a': a, 'b': b_adjusted, 'current_pos': half_space.get('current_pos')}))

            return adjusted_allocation

    def _extract_half_spaces(self, allocation: List[Tuple[float, dict]],
                             agent) -> List[Tuple[float, dict]]:
        half_spaces = []
        for t, agreement in allocation:
            pos = agent.get_position_at_time(t) if hasattr(agent, 'get_position_at_time') else [0, 0]
            half_spaces.append((t, {'a': agreement['a'], 'b': agreement['b'], 'current_pos': pos}))
        return half_spaces

    def entropy_guided_allocation_update(self, agent_i, agent_j,
                                         current_allocation: List[Tuple[float, dict]],
                                         new_trajectory_i: dict,
                                         new_trajectory_j: dict) -> List[Tuple[float, dict]]:
        return self.optimize_allocation(agent_i, agent_j, current_allocation, new_trajectory_i, new_trajectory_j)

    def get_entropy_trend(self, agent_id: int, entropy_type: str,
                          window: int = 5) -> Optional[str]:
        """Linear trend estimation for entropy prediction."""
        if agent_id not in self.entropy_history:
            return None
        history = self.entropy_history[agent_id].get(entropy_type, deque())
        if len(history) < window:
            return None
        recent = list(history)[-window:]
        slope = np.polyfit(range(len(recent)), recent, 1)[0]
        if slope > 0.1:   return 'increasing'
        elif slope < -0.1: return 'decreasing'
        else:              return 'stable'

    def reset(self):
        with self._lock:
            self.spatial_volumes.clear()
            self.velocity_profiles.clear()
            self.renewal_times.clear()
            self.entropy_history.clear()
            self._velocity_buffer.clear()
            self._comm_buffer.clear()
            self._comm_bins_learned = False
            self.comm_bins = None


entropy_manager = EntropyManager(
    alpha=1.0,
    beta=0.15,
    gamma=0.05,
    delta=0.02,
    adaptive_thresholds=True
)