# import numpy as np

# # ====== Three concentric circles crossing configuration ======
# NUM_AGENTS = 60  # Total 60 agents

# # Configuration for three circles
# circles = [
#     {'radius': 10, 'num_agents': 30, 'name': 'outer'},
#     {'radius': 7, 'num_agents': 20, 'name': 'middle'},
#     {'radius': 4, 'num_agents': 10, 'name': 'inner'},
# ]

# print(f"Generating three-circle concentric crossing scenario (total {NUM_AGENTS} agents)...")

# agent_list = []
# agent_index = 0

# for circle_idx, circle in enumerate(circles):
#     radius = circle['radius']
#     num_agents = circle['num_agents']
#     circle_name = circle['name']
    
#     print(f"\n{circle_name} (radius={radius}m, agents={num_agents})")
    
#     for i in range(num_agents):
#         angle = 2.0 * np.pi * i / num_agents
        
#         start_x = radius * np.cos(angle)
#         start_y = radius * np.sin(angle)
        
#         target_x = -start_x
#         target_y = -start_y
        
#         if circle_idx == 2:
#             response_type = agent_index % 3
#             if response_type == 0:
#                 t_w_base, t_c_base = 0.09, 0.07
#             elif response_type == 1:
#                 t_w_base, t_c_base = 0.14, 0.10
#             else:
#                 t_w_base, t_c_base = 0.18, 0.14
        
#         elif circle_idx == 1:
#             response_type = agent_index % 3
#             if response_type == 0:
#                 t_w_base, t_c_base = 0.12, 0.09
#             elif response_type == 1:
#                 t_w_base, t_c_base = 0.15, 0.11
#             else:
#                 t_w_base, t_c_base = 0.19, 0.15
        
#         else:
#             response_type = agent_index % 3
#             if response_type == 0:
#                 t_w_base, t_c_base = 0.14, 0.10
#             elif response_type == 1:
#                 t_w_base, t_c_base = 0.17, 0.13
#             else:
#                 t_w_base, t_c_base = 0.21, 0.16
        
#         t_w = t_w_base + (agent_index % 5) * 0.01
#         t_c = t_c_base + (agent_index % 4) * 0.01
        
#         robot_type = 'Mini_om'
        
#         agent_list.append({
#             'index': agent_index,
#             'K': 23,
#             'h': 0.1,
#             't_w': t_w,
#             't_c': t_c,
#             'type': robot_type,
#             'state': np.array([start_x, start_y]),
#             'tar': np.array([target_x, target_y]),
#         })
        
#         if i < 3 or i == num_agents - 1:
#             print(f"  Agent {agent_index}: angle={np.degrees(angle):.1f}deg "
#                   f"start=({start_x:.2f}, {start_y:.2f}) "
#                   f"target=({target_x:.2f}, {target_y:.2f}) "
#                   f"type={robot_type}")
        
#         agent_index += 1

# obstacle_list = [
#     {
#         'position': [0.0, 0.0],
#         'shape': [0.1],
#         'rotation': 0.0,
#         'type': 'circle'
#     },
# ]

# print(f"\nConfiguration generation completed:")
# print(f"  - Total agents: {len(agent_list)}")
# print(f"  - Outer (r={circles[0]['radius']}m): {circles[0]['num_agents']}")
# print(f"  - Middle (r={circles[1]['radius']}m): {circles[1]['num_agents']}")
# print(f"  - Inner (r={circles[2]['radius']}m): {circles[2]['num_agents']}")

# for circle_idx, circle in enumerate(circles):
#     num_agents = circle['num_agents']
#     angles = [2.0 * np.pi * i / num_agents for i in range(num_agents)]
#     print(f"  - {circle['name']} angular interval: {360/num_agents:.2f}deg")

# positions = set()
# duplicates = 0
# for agent in agent_list:
#     pos_key = (round(agent['state'][0], 2), round(agent['state'][1], 2))
#     if pos_key in positions:
#         duplicates += 1
#     positions.add(pos_key)

# if duplicates > 0:
#     print(f"  Warning: {duplicates} duplicate positions detected!")
# else:
#     print(f"  All agent positions unique")

# mini_om_count = sum(1 for a in agent_list if a['type'] == 'Mini_om')
# print(f"  - Vehicle types: Mini_om={mini_om_count} (all)")

# import numpy as np
# Scenario experimental setting
# # ====== Configuration parameters ======
# radius = 9
# NUM_AGENTS = 64

# print(f"Generating {NUM_AGENTS} agent configurations...")

# agent_list = []

# for i in range(NUM_AGENTS):
#     angle = 2.0 * np.pi * i / NUM_AGENTS
    
#     start_x = radius * np.cos(angle)
#     start_y = radius * np.sin(angle)
    
#     target_x = -start_x
#     target_y = -start_y
    
#     response_type = i % 3
    
#     if response_type == 0:
#         t_w_base, t_c_base = 0.09, 0.07
#     elif response_type == 1:
#         t_w_base, t_c_base = 0.14, 0.10
#     else:
#         t_w_base, t_c_base = 0.18, 0.14
    
#     t_w = t_w_base + (i % 5) * 0.01
#     t_c = t_c_base + (i % 4) * 0.01
    
#     agent_list.append({
#         'index': i,
#         'K': 23,
#         'h': 0.1,
#         't_w': t_w,
#         't_c': t_c,
#         'type': 'Mini_om',
#         'state': np.array([start_x, start_y]),
#         'tar': np.array([target_x, target_y]),
#     })
    
#     if i < 3 or i == NUM_AGENTS - 1:
#         print(f"  Agent {i}: angle={np.degrees(angle):.1f}deg "
#               f"start=({start_x:.2f}, {start_y:.2f}) "
#               f"target=({target_x:.2f}, {target_y:.2f})")

# obstacle_list = [
#     {
#         'position': [0.0, 0.0],
#         'shape': [0.1],
#         'rotation': 0.0,
#         'type': 'circle'
#     },
# ]

# print(f"\nConfiguration generation completed:")
# print(f"  - Number of agents: {len(agent_list)}")
# print(f"  - Circle radius: {radius}m")
# print(f"  - Angular interval: {360/NUM_AGENTS:.2f}deg")

# angles = [2.0 * np.pi * i / NUM_AGENTS for i in range(NUM_AGENTS)]
# print(f"  - Angle range: {np.degrees(min(angles)):.1f}deg ~ {np.degrees(max(angles)):.1f}deg")

# positions = set()
# duplicates = 0
# for agent in agent_list:
#     pos_key = (round(agent['state'][0], 2), round(agent['state'][1], 2))
#     if pos_key in positions:
#         duplicates += 1
#     positions.add(pos_key)

# if duplicates > 0:
#     print(f"  Warning: {duplicates} duplicate positions detected!")
# else:
#     print(f"  All agent positions unique")

import numpy as np

# ====== 8-Agent Configuration ======
radius = 4.0  

agent_list = [
    # ============================================
    # Agent 1: Bicycle (Index 1 in paper)
    # ============================================
    {
        'index': 0,  # Program index starts from 0, corresponding to Index 1 in paper
        'K': 20,
        'h': 0.15,
        't_w': 0.09,
        't_c': 0.07,
        'type': 'Mini_ack',  # Bicycle - Ackermann steering
        'state': np.array([radius, 0.0, np.pi]),    # Right side, facing left
        'tar': np.array([-radius, 0.0, np.pi]),     # Left side
    },
    
    # ============================================
    # Agent 2: Double Integrator (Index 2)
    # ============================================
    {
        'index': 1,
        'K': 20,
        'h': 0.15,
        't_w': 0.14,
        't_c': 0.12,
        'type': 'Mini_mec',  # Double Integrator - Mecanum wheel
        'state': np.array([radius*0.707, radius*0.707, np.pi/4]),
        'tar': np.array([-radius*0.707, -radius*0.707, 5*np.pi/4]),
    },
    
    # ============================================
    # Agent 3: Unicycle (Index 3)
    # ============================================
    {
        'index': 2,
        'K': 20,
        'h': 0.15,
        't_w': 0.21,
        't_c': 0.16,
        'type': 'Mini_4wd',  # Unicycle - 4WD differential
        'state': np.array([0.0, radius, np.pi/2]),
        'tar': np.array([0.0, -radius, 3*np.pi/2]),
    },
    
    # ============================================
    # Agent 4: Double Integrator (Index 4)
    # ============================================
    {
        'index': 3,
        'K': 20,
        'h': 0.15,
        't_w': 0.17,
        't_c': 0.10,
        'type': 'Mini_om',  # Double Integrator - Omni wheel
        'state': np.array([-radius*0.707, radius*0.707, 3*np.pi/4]),
        'tar': np.array([radius*0.707, -radius*0.707, 7*np.pi/4]),
    },
    
    # ============================================
    # Agent 5: Bicycle (Index 5)
    # ============================================
    {
        'index': 4,
        'K': 20,
        'h': 0.15,
        't_w': 0.10,
        't_c': 0.08,
        'type': 'Mini_ack',  # Bicycle - Ackermann steering
        'state': np.array([-radius, 0.0, 0.0]),
        'tar': np.array([radius, 0.0, 0.0]),
    },
    
    # ============================================
    # Agent 6: Double Integrator (Index 6)
    # ============================================
    {
        'index': 5,
        'K': 20,
        'h': 0.15,
        't_w': 0.14,
        't_c': 0.10,
        'type': 'Mini_mec',  # Double Integrator - Mecanum wheel
        'state': np.array([-radius*0.707, -radius*0.707, 5*np.pi/4]),
        'tar': np.array([radius*0.707, radius*0.707, np.pi/4]),
    },
    
    # ============================================
    # Agent 7: Unicycle (Index 7)
    # ============================================
    {
        'index': 6,
        'K': 20,
        'h': 0.15,
        't_w': 0.16,
        't_c': 0.12,
        'type': 'Mini_tank',  # Unicycle - Tank chassis
        'state': np.array([0.0, -radius, 3*np.pi/2]),
        'tar': np.array([0.0, radius, np.pi/2]),
    },
    
    # ============================================
    # Agent 8: Unicycle (Index 8)
    # ============================================
    {
        'index': 7,
        'K': 20,
        'h': 0.15,
        't_w': 0.18,
        't_c': 0.16,
        'type': 'Mini_4wd',  # Unicycle - 4WD differential
        'state': np.array([radius*0.707, -radius*0.707, 7*np.pi/4]),
        'tar': np.array([-radius*0.707, radius*0.707, 3*np.pi/4]),
    },
]

# ====== Obstacle configuration (4 different shapes on critical paths) ======
obstacle_list = [
    # ============================================
    # Obstacle 1: Cylinder (center)
    # ============================================
    {
        'position': [0.0, 0.0],
        'shape': [0.15],
        'rotation': 0.0,
        'type': 'circle'
    },
    
    # ============================================
    # Obstacle 2: Square / rectangular prism (right)
    # ============================================
    {
        'position': [1.2, -0.8],
        'shape': [0.15],
        'rotation': np.pi/4,
        'type': 'rectangle'
    },
    
    # ============================================
    # Obstacle 3: Pentagonal prism (top)
    # ============================================
    {
        'position': [0.0, 1.4],
        'shape': [0.2],
        'rotation': -np.pi/2,
        'type': 'pentagon'
    },
    
    # ============================================
    # Obstacle 4: Rectangular prism (bottom-left)
    # ============================================
    {
        'position': [-1.2, -0.8],
        'shape': [0.18],
        'rotation': 0.0,
        'type': 'rectangle'
    },
]

# import numpy as np

# # ====== Paper scenario: 8 double integrator agents, 8.0m diameter circular crossing ======
# radius = 4.0 

# # Unified dynamics parameters
# MAX_VELOCITY = 1.0
# MAX_ACCELERATION = 1.5
# PLANNING_HORIZON = 2.3

# h_timestep = PLANNING_HORIZON / 20
# K_steps = 20

# agent_list = [
#     # ============================================
#     # Agent 1: Double Integrator (Table I Index 1)
#     # ============================================
#     {
#         'index': 0,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([radius, 0.0, np.pi]),
#         'tar': np.array([-radius, 0.0, np.pi]),
#     },
    
#     # ============================================
#     # Agent 2: Double Integrator (Table I Index 2)
#     # ============================================
#     {
#         'index': 1,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.14,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([radius*0.707, radius*0.707, -3*np.pi/4]),
#         'tar': np.array([-radius*0.707, -radius*0.707, 5*np.pi/4]),
#     },
    
#     # ============================================
#     # Agent 3: Double Integrator (Table I Index 3)
#     # ============================================
#     {
#         'index': 2,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.21,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([0.0, radius, np.pi/2]),
#         'tar': np.array([0.0, -radius, 3*np.pi/2]),
#     },
    
#     # ============================================
#     # Agent 4: Double Integrator (Table I Index 4)
#     # ============================================
#     {
#         'index': 3,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.17,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([-radius*0.707, radius*0.707, 3*np.pi/4]),
#         'tar': np.array([radius*0.707, -radius*0.707, 7*np.pi/4]),
#     },
    
#     # ============================================
#     # Agent 5: Double Integrator (Table I Index 5)
#     # ============================================
#     {
#         'index': 4,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.10,
#         't_c': 0.08,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([-radius, 0.0, 0.0]),
#         'tar': np.array([radius, 0.0, 0.0]),
#     },
    
#     # ============================================
#     # Agent 6: Double Integrator (Table I Index 6)
#     # ============================================
#     {
#         'index': 5,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.14,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([-radius*0.707, -radius*0.707, 5*np.pi/4]),
#         'tar': np.array([radius*0.707, radius*0.707, np.pi/4]),
#     },
    
#     # ============================================
#     # Agent 7: Double Integrator (Table I Index 7)
#     # ============================================
#     {
#         'index': 6,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.16,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([0.0, -radius, 3*np.pi/2]),
#         'tar': np.array([0.0, radius, np.pi/2]),
#     },
    
#     # ============================================
#     # Agent 8: Double Integrator (Table I Index 8)
#     # ============================================
#     {
#         'index': 7,
#         'K': K_steps,
#         'h': h_timestep,
#         't_w': 0.18,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'max_vel': MAX_VELOCITY,
#         'max_acc': MAX_ACCELERATION,
#         'state': np.array([radius*0.707, -radius*0.707, 3*np.pi/4]),
#         'tar': np.array([-radius*0.707, radius*0.707, 3*np.pi/4]),
#     },
# ]

# # No obstacles
# obstacle_list = []

# import numpy as np

# # ====== 8 double integrator agents lane-change scenario ======
# # Scenario: 8 agents arranged vertically (1m spacing), moving right 8m and changing lanes
# # Agent 0 (bottom) <-> Agent 7 (top)
# # Agent 1 <-> Agent 6
# # Agent 2 <-> Agent 5  
# # Agent 3 <-> Agent 4

# LANE_DISTANCE = 8.0
# VERTICAL_SPACING = 1.0

# agent_list = [
#     # Agent 0: bottom -> top position
#     {
#         'index': 0,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 0.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 7.0 * VERTICAL_SPACING, 0.0]),
#     },
    
#     # Agent 1: 2nd from bottom -> 2nd from top
#     {
#         'index': 1,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 1.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 6.0 * VERTICAL_SPACING, 0.0]),
#     },
    
#     # Agent 2: 3rd from bottom -> 3rd from top
#     {
#         'index': 2,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.21,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 2.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 5.0 * VERTICAL_SPACING, 0.0]),
#     },
    
#     # Agent 3: 4th from bottom -> 4th from top
#     {
#         'index': 3,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.17,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 3.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 4.0 * VERTICAL_SPACING, 0.0]),
#     },
    
#     # Agent 4: 4th from top -> 4th from bottom
#     {
#         'index': 4,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.10,
#         't_c': 0.08,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 4.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 3.0 * VERTICAL_SPACING, 0.0]),
#     },
    
#     # Agent 5: 3rd from top -> 3rd from bottom
#     {
#         'index': 5,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 5.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 2.0 * VERTICAL_SPACING, 0.0]),
#     },
    
#     # Agent 6: 2nd from top -> 2nd from bottom
#     {
#         'index': 6,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.16,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 6.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 1.0 * VERTICAL_SPACING, 0.0]),
#     },
    
#     # Agent 7: top -> bottom position
#     {
#         'index': 7,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.18,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 7.0 * VERTICAL_SPACING, 0.0]),
#         'tar': np.array([LANE_DISTANCE, 0.0 * VERTICAL_SPACING, 0.0]),
#     },
# ]

# # No obstacles (pure lane-change scenario)
# obstacle_list = []

# import numpy as np

# # ====== 16 double integrator agents bidirectional lane-change ======
# # Left group: 8 agents moving right and changing lanes (Agent 0-7)
# # Right group: 8 agents moving left and changing lanes (Agent 8-15)

# LANE_DISTANCE = 8.0
# VERTICAL_SPACING = 1.0
# START_OFFSET = 0

# TRANSLATION_X = 0
# TRANSLATION_Y = 0

# agent_list = [
#     # Left group: Agent 0-7
#     # Agent 0
#     {
#         'index': 0,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 0.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 7.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
#     # Agent 1
#     {
#         'index': 1,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 1.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 6.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
#     # Agent 2
#     {
#         'index': 2,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.21,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 2.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 5.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
#     # Agent 3
#     {
#         'index': 3,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.17,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 3.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 4.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
#     # Agent 4
#     {
#         'index': 4,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.10,
#         't_c': 0.08,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 4.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 3.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
#     # Agent 5
#     {
#         'index': 5,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 5.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 2.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
#     # Agent 6
#     {
#         'index': 6,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.16,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 6.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 1.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
#     # Agent 7
#     {
#         'index': 7,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.18,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0 + TRANSLATION_X, 7.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#         'tar': np.array([LANE_DISTANCE + TRANSLATION_X, 0.0 * VERTICAL_SPACING + TRANSLATION_Y, 0.0]),
#     },
    
#     # Right group: Agent 8-15
#     # Agent 8
#     {
#         'index': 8,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.11,
#         't_c': 0.09,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 0.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 7.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
#     # Agent 9
#     {
#         'index': 9,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.15,
#         't_c': 0.13,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 1.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 6.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
#     # Agent 10
#     {
#         'index': 10,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.22,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 2.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 5.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
#     # Agent 11
#     {
#         'index': 11,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.20,
#         't_c': 0.19,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 3.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 4.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
#     # Agent 12
#     {
#         'index': 12,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.12,
#         't_c': 0.09,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 4.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 3.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
#     # Agent 13
#     {
#         'index': 13,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.15,
#         't_c': 0.11,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 5.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 2.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
#     # Agent 14
#     {
#         'index': 14,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.17,
#         't_c': 0.13,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 6.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 1.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
#     # Agent 15
#     {
#         'index': 15,
#         'K': 30,
#         'h': 0.15,
#         't_w': 0.20,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET + TRANSLATION_X, 7.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#         'tar': np.array([START_OFFSET + TRANSLATION_X, 0.0 * VERTICAL_SPACING + TRANSLATION_Y, np.pi]),
#     },
# ]

# obstacle_list = []

# """
# ====== Unsignalized intersection scenario ======
# """

# import numpy as np

# LANE_WIDTH = 0.5
# MEDIAN_WIDTH = 0.15
# APPROACH_DISTANCE = 3.5

# ENABLE_OBSTACLES = True

# road_half_width = MEDIAN_WIDTH/2 + 3 * LANE_WIDTH  # 1.575m

# SCALE = 0.85

# agent_list = [
#     # Car 1: Eastbound left turn (-2.5, -0.5) -> (0.5, 2.5)
#     {
#         'index': 0, 'K': 25, 'h': 0.15, 't_w': 0.09, 't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-2.5*SCALE, -0.5*SCALE, 0.0]),      # East (0deg)
#         'tar': np.array([0.5*SCALE, 2.75*SCALE, np.pi/2]),      # North (90deg)
#     },
#     # Car 2: Eastbound straight (-2.5, -1.0) -> (2.5, -1.0)
#     {
#         'index': 1, 'K': 25, 'h': 0.15, 't_w': 0.10, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([-2.5*SCALE, -1.0*SCALE, 0.0]),
#         'tar': np.array([2.75*SCALE, -1.0*SCALE, 0.0]),
#     },
#     # Car 3: Eastbound right turn (-2.5, -1.5) -> (-1.5, -2.5)
#     {
#         'index': 2, 'K': 25, 'h': 0.15, 't_w': 0.12, 't_c': 0.09,
#         'type': 'Mini_ack',
#         'state': np.array([-2.5*SCALE, -1.5*SCALE, 0.0]),
#         'tar': np.array([-1.5*SCALE, -2.75*SCALE, -np.pi/2]),
#     },
    
#     # Car 4: Northbound left turn (0.5, -2.5) -> (-2.5, 0.5)
#     {
#         'index': 3, 'K': 25, 'h': 0.15, 't_w': 0.09, 't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([0.5*SCALE, -2.5*SCALE, np.pi/2]),
#         'tar': np.array([-2.75*SCALE, 0.5*SCALE, np.pi]),
#     },
#     # Car 5: Northbound straight (1.0, -2.5) -> (1.0, 2.5)
#     {
#         'index': 4, 'K': 25, 'h': 0.15, 't_w': 0.10, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([1.0*SCALE, -2.5*SCALE, np.pi/2]),
#         'tar': np.array([1.0*SCALE, 2.75*SCALE, np.pi/2]),
#     },
#     # Car 6: Northbound right turn (1.5, -2.5) -> (2.5, -1.5)
#     {
#         'index': 5, 'K': 25, 'h': 0.15, 't_w': 0.12, 't_c': 0.09,
#         'type': 'Mini_ack',
#         'state': np.array([1.5*SCALE, -2.5*SCALE, np.pi/2]),
#         'tar': np.array([2.75*SCALE, -1.5*SCALE, 0.0]),
#     },
    
#     # Car 7: Westbound left turn (2.5, 0.5) -> (-0.5, -2.5)
#     {
#         'index': 6, 'K': 40, 'h': 0.15, 't_w': 0.09, 't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([2.5*SCALE, 0.5*SCALE, np.pi]),
#         'tar': np.array([-0.5*SCALE, -2.75*SCALE]), 
#         'free_orientation': True,
#     },
#     # Car 8: Westbound straight (2.5, 1.0) -> (-2.5, 1.0)
#     {
#         'index': 7, 'K': 25, 'h': 0.15, 't_w': 0.10, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([2.5*SCALE, 1.0*SCALE, np.pi]),
#         'tar': np.array([-2.75*SCALE, 1.0*SCALE, np.pi]),
#     },
#     # Car 9: Westbound right turn (2.5, 1.5) -> (1.5, 2.5)
#     {
#         'index': 8, 'K': 25, 'h': 0.15, 't_w': 0.12, 't_c': 0.09,
#         'type': 'Mini_ack',
#         'state': np.array([2.5*SCALE, 1.5*SCALE, np.pi]),
#         'tar': np.array([1.5*SCALE, 2.75*SCALE, np.pi/2]),
#     },
    
#     # Car 10: Southbound left turn (-0.5, 2.5) -> (2.5, -0.5)
#     {
#         'index': 9, 'K': 25, 'h': 0.15, 't_w': 0.09, 't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-0.5*SCALE, 2.5*SCALE, -np.pi/2]),
#         'tar': np.array([2.75*SCALE, -0.5*SCALE, 0.0]),
#     },
#     # Car 11: Southbound straight (-1.0, 2.5) -> (-1.0, -2.5)
#     {
#         'index': 10, 'K': 25, 'h': 0.15, 't_w': 0.10, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([-1.0*SCALE, 2.5*SCALE, -np.pi/2]),
#         'tar': np.array([-1.0*SCALE, -2.75*SCALE, -np.pi/2]),
#     },
#     # Car 12: Southbound right turn (-1.5, 2.5) -> (-2.5, 1.5)
#     {
#         'index': 11, 'K': 25, 'h': 0.15, 't_w': 0.12, 't_c': 0.09,
#         'type': 'Mini_ack',
#         'state': np.array([-1.5*SCALE, 2.5*SCALE, -np.pi/2]),
#         'tar': np.array([-2.75*SCALE, 1.5*SCALE, -np.pi]),
#     },
# ]

# def get_intersection_obstacles():
#     """Generate obstacles for an unsignalized intersection"""
#     BARRIER_THICKNESS = 0.08
#     MEDIAN_THICKNESS = 0.06
    
#     CORNER_EXPANSION = 0.4
    
#     expanded_road_half_width = road_half_width + CORNER_EXPANSION
    
#     barrier_length = APPROACH_DISTANCE - expanded_road_half_width - 0.2
#     barrier_start = expanded_road_half_width + 0.1
    
#     corner_size = road_half_width - 0.1
#     corner_offset = road_half_width + corner_size + CORNER_EXPANSION
    
#     median_start = corner_offset - corner_size
#     median_length = APPROACH_DISTANCE - median_start - 0.15
    
#     obstacles = [
#         # Corner blocks (brown)
#         {'position': [corner_offset, corner_offset], 'shape': [corner_size, corner_size],
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'brown', 'name': 'corner_NE'},
#         {'position': [-corner_offset, corner_offset], 'shape': [corner_size, corner_size],
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'brown', 'name': 'corner_NW'},
#         {'position': [corner_offset, -corner_offset], 'shape': [corner_size, corner_size],
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'brown', 'name': 'corner_SE'},
#         {'position': [-corner_offset, -corner_offset], 'shape': [corner_size, corner_size],
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'brown', 'name': 'corner_SW'},
        
#         # Road boundaries (green)
#         {'position': [barrier_start + barrier_length/2, expanded_road_half_width], 
#          'shape': [barrier_length/2, BARRIER_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_EW_N_E'},
#         {'position': [-(barrier_start + barrier_length/2), expanded_road_half_width], 
#          'shape': [barrier_length/2, BARRIER_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_EW_N_W'},
#         {'position': [barrier_start + barrier_length/2, -expanded_road_half_width], 
#          'shape': [barrier_length/2, BARRIER_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_EW_S_E'},
#         {'position': [-(barrier_start + barrier_length/2), -expanded_road_half_width], 
#          'shape': [barrier_length/2, BARRIER_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_EW_S_W'},
#         {'position': [expanded_road_half_width, barrier_start + barrier_length/2], 
#          'shape': [BARRIER_THICKNESS, barrier_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_NS_E_N'},
#         {'position': [expanded_road_half_width, -(barrier_start + barrier_length/2)], 
#          'shape': [BARRIER_THICKNESS, barrier_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_NS_E_S'},
#         {'position': [-expanded_road_half_width, barrier_start + barrier_length/2], 
#          'shape': [BARRIER_THICKNESS, barrier_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_NS_W_N'},
#         {'position': [-expanded_road_half_width, -(barrier_start + barrier_length/2)], 
#          'shape': [BARRIER_THICKNESS, barrier_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_NS_W_S'},
        
#         # Median strips (yellow)
#         {'position': [median_start + median_length/2, 0], 
#          'shape': [median_length/2, MEDIAN_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'yellow', 'name': 'median_E'},
#         {'position': [-(median_start + median_length/2), 0], 
#          'shape': [median_length/2, MEDIAN_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'yellow', 'name': 'median_W'},
#         {'position': [0, median_start + median_length/2], 
#          'shape': [MEDIAN_THICKNESS, median_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'yellow', 'name': 'median_N'},
#         {'position': [0, -(median_start + median_length/2)], 
#          'shape': [MEDIAN_THICKNESS, median_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'yellow', 'name': 'median_S'},
#     ]
#     return obstacles

# if ENABLE_OBSTACLES:
#     obstacle_list = get_intersection_obstacles()
# else:
#     obstacle_list = []

# """
# ====== T-intersection scenario ======
# """

# import numpy as np

# LANE_WIDTH = 0.5
# MEDIAN_WIDTH = 0.15
# APPROACH_DISTANCE = 3.5

# ENABLE_OBSTACLES = True

# road_half_width = MEDIAN_WIDTH/2 + 3 * LANE_WIDTH  # 1.575m

# SCALE = 1

# agent_list = [
#     # Car 1
#     {
#         'index': 0, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([-2.1*SCALE, -0.5*SCALE, 0.0]),
#         'tar': np.array([-2.1*SCALE, 1.5*SCALE, np.pi]),
#     },
#     # Car 2: Westbound left turn (-2.5, -1.0) -> (1.0, 2.5)
#     {
#         'index': 1, 'K': 15, 'h': 0.15, 't_w': 0.10, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([-2.1*SCALE, -1.0*SCALE, 0.0]),
#         'tar': np.array([0.5*SCALE, 2.8*SCALE, np.pi/2]),
#     },
#     # Car 3: Westbound right turn (-2.1, -1.5) -> (-1.5, -2.1)
#     {
#         'index': 2, 'K': 15, 'h': 0.15, 't_w': 0.12, 't_c': 0.09,
#         'type': 'Mini_ack',
#         'state': np.array([-2.1*SCALE, -1.5*SCALE, 0]),
#         'tar': np.array([-0.5*SCALE, -2.8*SCALE, -np.pi/2]),
#     },
    
#     # Car 4: Northbound U-turn (0.5, -2.1) -> (-0.5, -2.1)
#     {
#         'index': 3, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([0.5*SCALE, -2.1*SCALE, np.pi/2]),
#         'tar': np.array([1.0*SCALE, 2.1*SCALE, -np.pi/2]),
#         'free_orientation': True,
#     },
#     # Car 5: Northbound left turn (1.0, -2.1) -> (-2.1, 1.0)
#     {
#         'index': 4, 'K': 15, 'h': 0.15, 't_w': 0.10, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([0.9*SCALE, -2.1*SCALE, np.pi/2]),
#         'tar': np.array([-2.8*SCALE, 1.0*SCALE, np.pi]),
#     },
#     # Car 6: Northbound straight (1.5, -2.1) -> (1.5, 2.1) 
#     {
#         'index': 5, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([1.3*SCALE, -2.1*SCALE, np.pi/2]),
#         'tar': np.array([-1.5*SCALE, -2.6*SCALE, -np.pi/2]),
#     },
    
#     # Car 7: Southbound U-turn (-0.5, 2.1) -> (0.5, 2.1)
#     {
#         'index': 6, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-0.5*SCALE, 2.1*SCALE, -np.pi/2]),
#         'tar': np.array([-1.0*SCALE, -2.8*SCALE, -np.pi/2]),
#     },
#     # Car 8: Southbound straight (-1.0, 2.1) -> (-1.0, -2.1)
#     {
#         'index': 7, 'K': 10, 'h': 0.15, 't_w': 0.10, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([-1.0*SCALE, 2.1*SCALE, -np.pi/2]),
#         'tar': np.array([-2.1*SCALE, 0.5*SCALE, -7*np.pi/8]),
#     },
#     # Car 9: Southbound right turn (-1.5, 2.1) -> (-2.1, 1.5)
#     {
#         'index': 8, 'K': 15, 'h': 0.15, 't_w': 0.12, 't_c': 0.09,
#         'type': 'Mini_ack',
#         'state': np.array([-1.5*SCALE, 2.1*SCALE, -np.pi/2]),
#         'tar': np.array([1.5*SCALE, 2.1*SCALE, np.pi/2]),
#     },

#     # Car 10
#     {
#         'index': 9, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([-0.5*SCALE, 2.8*SCALE, -np.pi/2]),
#         'tar': np.array([-1.0*SCALE, -2.1*SCALE, -np.pi/2]),
#     },

#     # Car 11
#     {
#         'index': 10, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([-1.0*SCALE, 2.8*SCALE, -np.pi/2]),
#         'tar': np.array([-0.5*SCALE, -2.1*SCALE, -np.pi/2]),
#     },

#     # Car 12
#     {
#         'index': 11, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([0.5*SCALE, -2.8*SCALE, np.pi/2]),
#         'tar': np.array([-2.1*SCALE, 1.0*SCALE, np.pi]),
#         'start_delay': 5.0,
#     },

#     # Car 13
#     {
#         'index': 12, 'K': 15, 'h': 0.15, 't_w': 0.09, 't_c': 0.08,
#         'type': 'Mini_ack',
#         'state': np.array([0.9*SCALE, -2.8*SCALE, np.pi/2]),
#         'tar': np.array([0.5*SCALE, 2.1*SCALE, np.pi/2]),
#         'start_delay': 5.0,
#     },
# ]

# def get_t_intersection_obstacles():
#     """Generate obstacles for a T-intersection (east branch removed)"""
#     BARRIER_THICKNESS = 0.08
#     MEDIAN_THICKNESS = 0.06
    
#     CORNER_EXPANSION = 0.4
    
#     expanded_road_half_width = road_half_width + CORNER_EXPANSION
    
#     barrier_length = APPROACH_DISTANCE - expanded_road_half_width - 0.2
#     barrier_start = expanded_road_half_width + 0.1
    
#     corner_size = road_half_width - 0.1
#     corner_offset = road_half_width + corner_size + CORNER_EXPANSION
    
#     median_start = corner_offset - corner_size
#     median_length = APPROACH_DISTANCE - median_start - 0.15
    
#     obstacles = [
#         # Corners (brown) - keep west, north, south corners
#         {'position': [-corner_offset, corner_offset], 'shape': [corner_size, corner_size],
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'brown', 'name': 'corner_NW'},
#         {'position': [-corner_offset, -corner_offset], 'shape': [corner_size, corner_size],
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'brown', 'name': 'corner_SW'},
        
#         # East wall (brown) replacing northeast and southeast corners
#         {'position': [corner_offset, 0], 
#          'shape': [corner_size, 1.45*corner_offset], 
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'brown', 'name': 'east_wall'},
        
#         # Road boundaries (green) - remove east side, keep west, north, south
#         {'position': [-(barrier_start + barrier_length/2), expanded_road_half_width], 
#          'shape': [barrier_length/2, BARRIER_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_EW_N_W'},
#         {'position': [-(barrier_start + barrier_length/2), -expanded_road_half_width], 
#          'shape': [barrier_length/2, BARRIER_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_EW_S_W'},
        
#         # East vertical barrier (green)
#         {'position': [expanded_road_half_width, 0], 
#          'shape': [BARRIER_THICKNESS, 2*expanded_road_half_width], 
#          'rotation': 0.0, 'type': 'rectangle', 'color': 'green', 'name': 'barrier_E_vertical'},
        
#         {'position': [-expanded_road_half_width, barrier_start + barrier_length/2], 
#          'shape': [BARRIER_THICKNESS, barrier_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_NS_W_N'},
#         {'position': [-expanded_road_half_width, -(barrier_start + barrier_length/2)], 
#          'shape': [BARRIER_THICKNESS, barrier_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'green', 'name': 'barrier_NS_W_S'},
        
#         # Median strips (yellow) - remove east side, keep west, north, south
#         {'position': [-(median_start + median_length/2), 0], 
#          'shape': [median_length/2, MEDIAN_THICKNESS], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'yellow', 'name': 'median_W'},
#         {'position': [0, median_start + median_length/2], 
#          'shape': [MEDIAN_THICKNESS, median_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'yellow', 'name': 'median_N'},
#         {'position': [0, -(median_start + median_length/2)], 
#          'shape': [MEDIAN_THICKNESS, median_length/2], 'rotation': 0.0, 
#          'type': 'rectangle', 'color': 'yellow', 'name': 'median_S'},
#     ]
#     return obstacles

# if ENABLE_OBSTACLES:
#     obstacle_list = get_t_intersection_obstacles()
# else:
#     obstacle_list = []

# import numpy as np

# # ====== 16 double integrator agents bidirectional lane-change with custom pairing ======
# # Left 8 agents move right and change lanes (Agent 0-7)
# # Right 8 agents move left and change lanes (Agent 8-15)
# # Crossing trajectories form an X shape to distribute conflicts.

# LANE_DISTANCE = 8.0
# VERTICAL_SPACING = 1.0
# START_OFFSET = 1.0

# agent_list = [
#     # Left group: Agent 0-7
#     # Agent 0 (y=0) -> target y=3
#     {
#         'index': 0,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 0.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 3.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 1 (y=1) -> target y=4
#     {
#         'index': 1,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 1.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 4.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 2 (y=2) -> target y=5
#     {
#         'index': 2,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.21,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 2.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 5.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 3 (y=3) -> target y=6
#     {
#         'index': 3,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.17,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 3.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 6.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 4 (y=4) -> target y=1
#     {
#         'index': 4,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.10,
#         't_c': 0.08,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 4.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 1.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 5 (y=5) -> target y=2
#     {
#         'index': 5,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 5.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 2.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 6 (y=6) -> target y=7
#     {
#         'index': 6,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.16,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 6.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 7.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 7 (y=7) -> target y=0
#     {
#         'index': 7,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.18,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 7.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 0.0 * VERTICAL_SPACING, 0.0]),
#     },

#     # Right group: Agent 8-15 (moving left, inverse mapping)
#     # Agent 8 (y=0) -> target y=7
#     {
#         'index': 8,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.11,
#         't_c': 0.09,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 0.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 7.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 9 (y=1) -> target y=4
#     {
#         'index': 9,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.15,
#         't_c': 0.13,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 1.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 4.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 10 (y=2) -> target y=5
#     {
#         'index': 10,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.22,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 2.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 5.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 11 (y=3) -> target y=0
#     {
#         'index': 11,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.19,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 3.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 0.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 12 (y=4) -> target y=1
#     {
#         'index': 12,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.12,
#         't_c': 0.09,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 4.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 1.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 13 (y=5) -> target y=2
#     {
#         'index': 13,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.15,
#         't_c': 0.11,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 5.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 2.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 14 (y=6) -> target y=3
#     {
#         'index': 14,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.17,
#         't_c': 0.13,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 6.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 3.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 15 (y=7) -> target y=6
#     {
#         'index': 15,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.20,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 7.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 6.0 * VERTICAL_SPACING, np.pi]),
#     },
# ]

# # Another pairing variant: diagonal pairing Agent i <-> Agent (15-i)
# LANE_DISTANCE = 8.0
# VERTICAL_SPACING = 1.0
# START_OFFSET = 1.0

# agent_list = [
#     # Left group: Agent 0-7
#     # Agent 0 (y=0) -> target y=7
#     {
#         'index': 0,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 0.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 7.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 1 (y=1) -> target y=6
#     {
#         'index': 1,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 1.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 6.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 2 (y=2) -> target y=5
#     {
#         'index': 2,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.21,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 2.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 5.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 3 (y=3) -> target y=4
#     {
#         'index': 3,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.17,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 3.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 4.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 4 (y=4) -> target y=3
#     {
#         'index': 4,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.10,
#         't_c': 0.08,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 4.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 3.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 5 (y=5) -> target y=2
#     {
#         'index': 5,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.14,
#         't_c': 0.10,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 5.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 2.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 6 (y=6) -> target y=1
#     {
#         'index': 6,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.16,
#         't_c': 0.12,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 6.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 1.0 * VERTICAL_SPACING, 0.0]),
#     },
#     # Agent 7 (y=7) -> target y=0
#     {
#         'index': 7,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.18,
#         't_c': 0.16,
#         'type': 'Mini_om',
#         'state': np.array([0.0, 7.0 * VERTICAL_SPACING, 0.0]),
#         'tar':   np.array([LANE_DISTANCE + START_OFFSET, 0.0 * VERTICAL_SPACING, 0.0]),
#     },

#     # Right group: Agent 8-15
#     # Agent 8 (y=0) -> target y=7
#     {
#         'index': 8,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.11,
#         't_c': 0.09,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 0.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 7.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 9 (y=1) -> target y=6
#     {
#         'index': 9,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.15,
#         't_c': 0.13,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 1.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 6.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 10 (y=2) -> target y=5
#     {
#         'index': 10,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.22,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 2.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 5.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 11 (y=3) -> target y=4
#     {
#         'index': 11,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.19,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 3.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 4.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 12 (y=4) -> target y=3
#     {
#         'index': 12,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.12,
#         't_c': 0.09,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 4.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 3.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 13 (y=5) -> target y=2
#     {
#         'index': 13,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.15,
#         't_c': 0.11,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 5.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 2.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 14 (y=6) -> target y=1
#     {
#         'index': 14,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.17,
#         't_c': 0.13,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 6.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 1.0 * VERTICAL_SPACING, np.pi]),
#     },
#     # Agent 15 (y=7) -> target y=0
#     {
#         'index': 15,
#         'K': 20,
#         'h': 0.15,
#         't_w': 0.20,
#         't_c': 0.17,
#         'type': 'Mini_om',
#         'state': np.array([LANE_DISTANCE + START_OFFSET, 7.0 * VERTICAL_SPACING, np.pi]),
#         'tar':   np.array([0.0, 0.0 * VERTICAL_SPACING, np.pi]),
#     },
# ]

# # No obstacles
# obstacle_list = []

# import numpy as np

# # ====== Roundabout scenario configuration (parameterized) ======

# OBSTACLE_CONFIG = {
#     'circle_radius': 2.0,
#     'radial_start_radius': 5.0,
#     'radial_length': 2.0,
#     'radial_thickness': 0.1,
#     'lane_width': 2.0,
#     'tangent_distance': 4.3,
#     'tangent_length': 0.7,
# }

# AGENT_CONFIG = {
#     'start_distance_from_center': 4.0,
#     'num_agents_per_lane': 2,
#     'agent_spacing_ratio': [1/3, 2/3],
#     'vehicle_type': 'Mini_ack',
#     'enable_destinations': True,
#     'destination_mode': 'symmetric',
# }

# ENABLE_OBSTACLES = True

# LANE_ANGLES = [np.pi/10, np.pi/2, 9*np.pi/10, -3*np.pi/10, -7*np.pi/10]

# def generate_agents():
#     """Generate agents with parameterized configuration.
#     Start positions are placed between the yellow centerline and left gray line.
#     Destinations are computed symmetrically across the yellow line.
#     """
#     agents = []
    
#     start_distance = AGENT_CONFIG['start_distance_from_center']
#     num_per_lane = AGENT_CONFIG['num_agents_per_lane']
#     spacing_ratios = AGENT_CONFIG['agent_spacing_ratio']
#     lane_width = OBSTACLE_CONFIG['lane_width']
#     vehicle_type = AGENT_CONFIG['vehicle_type']
#     enable_dest = AGENT_CONFIG['enable_destinations']
#     dest_mode = AGENT_CONFIG['destination_mode']
    
#     agent_index = 0
#     destination_registry = []
    
#     for lane_idx, angle in enumerate(LANE_ANGLES):
#         yellow_center_x = start_distance * np.cos(angle)
#         yellow_center_y = start_distance * np.sin(angle)
        
#         perpendicular_x = -np.sin(angle)
#         perpendicular_y = np.cos(angle)
        
#         left_offset_x = lane_width * perpendicular_x
#         left_offset_y = lane_width * perpendicular_y
        
#         for car_idx in range(num_per_lane):
#             if car_idx < len(spacing_ratios):
#                 t = spacing_ratios[car_idx]
#             else:
#                 t = (car_idx + 1) / (num_per_lane + 1)
            
#             start_x = yellow_center_x + t * left_offset_x
#             start_y = yellow_center_y + t * left_offset_y
            
#             start_theta = angle + np.pi
            
#             while start_theta > np.pi:
#                 start_theta -= 2 * np.pi
#             while start_theta < -np.pi:
#                 start_theta += 2 * np.pi
            
#             if enable_dest and dest_mode == 'symmetric':
#                 dest_x = yellow_center_x - t * left_offset_x
#                 dest_y = yellow_center_y - t * left_offset_y
                
#                 dest_theta = start_theta
                
#                 dest_key = (round(dest_x, 2), round(dest_y, 2))
#                 collision_count = 0
#                 while dest_key in destination_registry:
#                     collision_count += 1
#                     offset_dist = 0.3 * collision_count
#                     dest_x = yellow_center_x - t * left_offset_x + offset_dist * np.cos(angle)
#                     dest_y = yellow_center_y - t * left_offset_y + offset_dist * np.sin(angle)
#                     dest_key = (round(dest_x, 2), round(dest_y, 2))
                
#                 destination_registry.append(dest_key)
#             else:
#                 dest_x, dest_y, dest_theta = start_x, start_y, start_theta
            
#             agents.append({
#                 'index': agent_index,
#                 'K': 25,
#                 'h': 0.15,
#                 't_w': 0.09,
#                 't_c': 0.07,
#                 'type': vehicle_type,
#                 'state': np.array([start_x, start_y, start_theta]),
#                 'tar': np.array([dest_x, dest_y, dest_theta]),
#                 'lane': lane_idx + 1,
#                 'position': car_idx + 1,
#                 'start_distance': start_distance,
#             })
            
#             agent_index += 1
    
#     return agents

# agent_list = generate_agents()

# def get_roundabout_obstacles():
#     """Generate roundabout obstacles from OBSTACLE_CONFIG.
#     Includes a central circle, radial lines (yellow + two gray sides), and tangent lines.
#     """
#     obstacles = []
    
#     circle_radius = OBSTACLE_CONFIG['circle_radius']
#     radial_start = OBSTACLE_CONFIG['radial_start_radius']
#     radial_length = OBSTACLE_CONFIG['radial_length']
#     radial_thickness = OBSTACLE_CONFIG['radial_thickness']
#     lane_width = OBSTACLE_CONFIG['lane_width']
#     tangent_dist = OBSTACLE_CONFIG['tangent_distance']
#     tangent_len = OBSTACLE_CONFIG['tangent_length']
    
#     obstacles.append({
#         'position': [0.0, 0.0],
#         'shape': [circle_radius],
#         'rotation': 0.0,
#         'type': 'circle',
#         'color': 'brown',
#         'name': 'center_circle'
#     })
    
#     for idx, angle in enumerate(LANE_ANGLES):
#         start_x = radial_start * np.cos(angle)
#         start_y = radial_start * np.sin(angle)
#         end_x = (radial_start + radial_length) * np.cos(angle)
#         end_y = (radial_start + radial_length) * np.sin(angle)
        
#         center_x = (start_x + end_x) / 2
#         center_y = (start_y + end_y) / 2
        
#         obstacles.append({
#             'position': [center_x, center_y],
#             'shape': [radial_length, radial_thickness],
#             'rotation': angle,
#             'type': 'rectangle',
#             'color': 'yellow',
#             'name': f'radial_yellow_{idx+1}'
#         })
        
#         perpendicular_x = -np.sin(angle)
#         perpendicular_y = np.cos(angle)
        
#         left_offset_x = lane_width * perpendicular_x
#         left_offset_y = lane_width * perpendicular_y
        
#         obstacles.append({
#             'position': [center_x + left_offset_x, center_y + left_offset_y],
#             'shape': [radial_length, radial_thickness],
#             'rotation': angle,
#             'type': 'rectangle',
#             'color': 'gray',
#             'name': f'radial_gray_left_{idx+1}'
#         })
        
#         right_offset_x = -lane_width * perpendicular_x
#         right_offset_y = -lane_width * perpendicular_y
        
#         obstacles.append({
#             'position': [center_x + right_offset_x, center_y + right_offset_y],
#             'shape': [radial_length, radial_thickness],
#             'rotation': angle,
#             'type': 'rectangle',
#             'color': 'gray',
#             'name': f'radial_gray_right_{idx+1}'
#         })
    
#     tangent_angles = [3*np.pi/10, 7*np.pi/10, -np.pi/10, -5*np.pi/10, -9*np.pi/10]
    
#     for idx, angle in enumerate(tangent_angles):
#         tangent_point_x = circle_radius * np.cos(angle)
#         tangent_point_y = circle_radius * np.sin(angle)
        
#         tangent_rotation = angle + np.pi/2
        
#         radial_offset = tangent_dist - circle_radius
#         line_center_x = tangent_point_x + radial_offset * np.cos(angle)
#         line_center_y = tangent_point_y + radial_offset * np.sin(angle)
        
#         obstacles.append({
#             'position': [line_center_x, line_center_y],
#             'shape': [tangent_len, radial_thickness],
#             'rotation': tangent_rotation,
#             'type': 'rectangle',
#             'color': 'gray',
#             'name': f'tangent_{idx+1}'
#         })
    
#     return obstacles

# if ENABLE_OBSTACLES:
#     obstacle_list = get_roundabout_obstacles()
# else:
#     obstacle_list = []

# import numpy as np

# # ====== Roundabout scenario with 10 manual agents (fixed positions) ======
# OBSTACLE_CONFIG = {
#     'circle_radius': 2.0,
#     'radial_start_radius': 5.0,
#     'radial_length': 2.0,
#     'radial_thickness': 0.05,
#     'lane_width': 2.0,
#     'tangent_distance': 4.4,
#     'tangent_length': 0.7,
# }

# ENABLE_OBSTACLES = True

# LANE_ANGLES = [np.pi/10, np.pi/2, 9*np.pi/10, -3*np.pi/10, -7*np.pi/10]

# agent_list = [
#     # Lane 1: Agents 0-1 (18deg)
#     # Agent 0: lane 1, position 1 (1/3)
#     {
#         'index': 0,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([3.392, 2.504, -9*np.pi/10]),
#         'tar': np.array([0.667, 4.000, np.pi/2]),
#     },
#     # Agent 1: lane 1, position 2 (2/3)
#     {
#         'index': 1,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([3.598, 1.870, -9*np.pi/10]),
#         'tar': np.array([-3.392, 2.504, 9*np.pi/10]),
#     },
    
#     # Lane 2: Agents 2-3 (90deg)
#     # Agent 2: lane 2, position 1 (1/3)
#     {
#         'index': 2,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-0.6667, 4.000, -np.pi/2]),
#         'tar': np.array([-3.4298, -2.4524, -7*np.pi/10]),
#     },
#     # Agent 3: lane 2, position 2 (2/3)
#     {
#         'index': 3,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-1.3333, 4.0000, -np.pi/2]),
#         'tar': np.array([-3.5982, 1.8701, 9*np.pi/10]),
#     },
    
#     # Lane 3: Agents 4-5 (162deg)
#     # Agent 4: lane 3, position 1 (1/3)
#     {
#         'index': 4,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-4.010, 0.6020, -np.pi/10]),
#         'tar': np.array([1.2725, -4.0198, -3*np.pi/10]),
#     },
#     # Agent 5: lane 3, position 2 (2/3)
#     {
#         'index': 5,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-4.2162, -0.05, -np.pi/10]),
#         'tar': np.array([-2.8905, -2.8442, -7*np.pi/10]),
#     },
    
#     # Lane 4: Agents 6-7 (-54deg)
#     # Agent 6: lane 4, position 1 (1/3)
#     {
#         'index': 6,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([3.4298, -2.4524, 7*np.pi/10]),
#         'tar': np.array([4.0102, 0.6020, np.pi/10]),
#     },
#     # Agent 7: lane 4, position 2 (2/3)
#     {
#         'index': 7,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([2.8905, -2.8442, 7*np.pi/10]),
#         'tar': np.array([1.6667, 4.000, np.pi/2]),
#     },
    
#     # Lane 5: Agents 8-9 (-126deg)
#     # Agent 8: lane 5, position 1 (1/3)
#     {
#         'index': 8,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-1.812, -3.6279, 3*np.pi/10]),
#         'tar': np.array([4.2163, -0.1, np.pi/10]),
#     },
#     # Agent 9: lane 5, position 2 (2/3)
#     {
#         'index': 9,
#         'K': 15,
#         'h': 0.15,
#         't_w': 0.09,
#         't_c': 0.07,
#         'type': 'Mini_ack',
#         'state': np.array([-1.2725, -4.0198, 3*np.pi/10]),
#         'tar': np.array([1.8118, -3.6279, -3*np.pi/10]),
#     },
# ]

# def get_roundabout_obstacles():
#     """Generate roundabout obstacles from OBSTACLE_CONFIG (thin lines variant)."""
#     obstacles = []
    
#     circle_radius = OBSTACLE_CONFIG['circle_radius']
#     radial_start = OBSTACLE_CONFIG['radial_start_radius']
#     radial_length = OBSTACLE_CONFIG['radial_length']
#     radial_thickness = OBSTACLE_CONFIG['radial_thickness']
#     lane_width = OBSTACLE_CONFIG['lane_width']
#     tangent_dist = OBSTACLE_CONFIG['tangent_distance']
#     tangent_len = OBSTACLE_CONFIG['tangent_length']
    
#     obstacles.append({
#         'position': [0.0, 0.0],
#         'shape': [circle_radius],
#         'rotation': 0.0,
#         'type': 'circle',
#         'color': 'brown',
#         'name': 'center_circle'
#     })
    
#     for idx, angle in enumerate(LANE_ANGLES):
#         start_x = radial_start * np.cos(angle)
#         start_y = radial_start * np.sin(angle)
#         end_x = (radial_start + radial_length) * np.cos(angle)
#         end_y = (radial_start + radial_length) * np.sin(angle)
        
#         center_x = (start_x + end_x) / 2
#         center_y = (start_y + end_y) / 2
        
#         obstacles.append({
#             'position': [center_x, center_y],
#             'shape': [radial_length, radial_thickness],
#             'rotation': angle,
#             'type': 'rectangle',
#             'color': 'yellow',
#             'name': f'radial_yellow_{idx+1}'
#         })
        
#         perpendicular_x = -np.sin(angle)
#         perpendicular_y = np.cos(angle)
        
#         left_offset_x = lane_width * perpendicular_x
#         left_offset_y = lane_width * perpendicular_y
        
#         obstacles.append({
#             'position': [center_x + left_offset_x, center_y + left_offset_y],
#             'shape': [radial_length, radial_thickness],
#             'rotation': angle,
#             'type': 'rectangle',
#             'color': 'gray',
#             'name': f'radial_gray_left_{idx+1}'
#         })
        
#         right_offset_x = -lane_width * perpendicular_x
#         right_offset_y = -lane_width * perpendicular_y
        
#         obstacles.append({
#             'position': [center_x + right_offset_x, center_y + right_offset_y],
#             'shape': [radial_length, radial_thickness],
#             'rotation': angle,
#             'type': 'rectangle',
#             'color': 'gray',
#             'name': f'radial_gray_right_{idx+1}'
#         })
    
#     tangent_angles = [3*np.pi/10, 7*np.pi/10, -np.pi/10, -5*np.pi/10, -9*np.pi/10]
    
#     for idx, angle in enumerate(tangent_angles):
#         tangent_point_x = circle_radius * np.cos(angle)
#         tangent_point_y = circle_radius * np.sin(angle)
        
#         tangent_rotation = angle + np.pi/2
        
#         radial_offset = tangent_dist - circle_radius
#         line_center_x = tangent_point_x + radial_offset * np.cos(angle)
#         line_center_y = tangent_point_y + radial_offset * np.sin(angle)
        
#         obstacles.append({
#             'position': [line_center_x, line_center_y],
#             'shape': [tangent_len, radial_thickness],
#             'rotation': tangent_rotation,
#             'type': 'rectangle',
#             'color': 'gray',
#             'name': f'tangent_{idx+1}'
#         })
    
#     return obstacles

# if ENABLE_OBSTACLES:
#     obstacle_list = get_roundabout_obstacles()
# else:
#     obstacle_list = []