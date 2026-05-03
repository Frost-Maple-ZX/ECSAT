import numpy as np
from collections import defaultdict
import time


class CongestionPredictor:
    """
    Spatiotemporal congestion predictor implementing the local entropy map H_g .
    Discretizes agent trajectories onto a space-time grid with Gaussian smoothing.
    """

    def __init__(self, grid_size: float = 0.5, time_step: float = 0.3):
        self.grid_size = grid_size      # spatial resolution (m)
        self.time_step = time_step      # temporal resolution (s)

        self.congestion_map = defaultdict(float)
        self.agent_trajectories = {}

        self.last_update_time = 0
        self.update_interval = 0.5

    def update_agent_trajectory(self, agent_id: int, trajectory: dict, start_time: float):
        """Register a planned trajectory for agent_id."""
        self.agent_trajectories[agent_id] = {
            'x': np.array(trajectory['x']),
            'y': np.array(trajectory['y']),
            'start_time': start_time,
            'duration': trajectory.get('duration', 3.0)
        }

    def compute_congestion_map(self):
        """Build H_g via Gaussian-weighted trajectory occupancy."""
        current_time = time.time()
        if current_time - self.last_update_time < self.update_interval:
            return

        self.last_update_time = current_time
        self.congestion_map.clear()

        for agent_id, traj in self.agent_trajectories.items():
            x_list, y_list = traj['x'], traj['y']
            start_time, duration = traj['start_time'], traj['duration']
            n_points = len(x_list)
            if n_points < 2:
                continue

            dt = duration / max(n_points - 1, 1)
            for k in range(n_points):
                gx = int(np.round(x_list[k] / self.grid_size))
                gy = int(np.round(y_list[k] / self.grid_size))
                ts = int(np.round((start_time + k * dt) / self.time_step))

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        for dt_slot in [-1, 0, 1]:
                            weight = np.exp(-(dx ** 2 + dy ** 2 + dt_slot ** 2) / 2.0)
                            self.congestion_map[(gx + dx, gy + dy, ts + dt_slot)] += weight

    def get_congestion_at(self, x: float, y: float, t: float) -> float:
        """Query H_g at a given space-time location."""
        gx = int(np.round(x / self.grid_size))
        gy = int(np.round(y / self.grid_size))
        ts = int(np.round(t / self.time_step))
        return self.congestion_map.get((gx, gy, ts), 0.0)

    def compute_trajectory_congestion_cost(self, trajectory: dict, start_time: float):
        """
        Compute total congestion cost C_eta along a candidate trajectory.
        Returns (total_cost, max_congestion, congestion_profile).
        """
        x_list = np.array(trajectory['x'])
        y_list = np.array(trajectory['y'])
        duration = trajectory.get('duration', 3.0)
        n_points = len(x_list)

        if n_points < 2:
            return 0.0, 0.0, []

        dt = duration / max(n_points - 1, 1)
        total_cost, max_congestion, congestion_profile = 0.0, 0.0, []

        for k in range(n_points):
            congestion = self.get_congestion_at(x_list[k], y_list[k], start_time + k * dt)
            congestion_profile.append(congestion)
            max_congestion = max(max_congestion, congestion)

            # Piecewise penalty matching 
            if congestion > 3.0:
                total_cost += (congestion - 1.5) ** 1.5
            elif congestion > 2.0:
                total_cost += (congestion - 1.0) * 0.2

        return total_cost, max_congestion, congestion_profile

    def suggest_waiting_time(self, agent_pos: np.ndarray,
                             agent_target: np.ndarray,
                             current_time: float):
        """
        Estimate whether the agent should wait to reduce congestion cost .
        Returns (should_wait, suggested_delay_seconds).
        """
        direction = agent_target[:2] - agent_pos[:2]
        dist = np.linalg.norm(direction)
        if dist < 0.1:
            return False, 0.0

        direction = direction / dist
        congestion_now, congestion_later = [], []

        for i in range(10):
            sample_pos = agent_pos[:2] + direction * (i * 0.5)
            congestion_now.append(self.get_congestion_at(sample_pos[0], sample_pos[1], current_time))
            congestion_later.append(self.get_congestion_at(sample_pos[0], sample_pos[1], current_time + 1.0))

        avg_now = np.mean(congestion_now)
        avg_later = np.mean(congestion_later)

        if avg_now > 2.5 and avg_later < 1.8:
            delay = 0.7 + (avg_now - avg_later) * 0.3
            return True, min(delay, 1.5)
        return False, 0.0


congestion_predictor = CongestionPredictor(grid_size=0.5, time_step=0.3)