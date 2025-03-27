
import numpy as np
import matplotlib.pyplot as plt

# Constants
earth_radius = 6378  # km
altitude = 400  # km
start_distance = earth_radius + altitude  # 6778 km
gravity_constant = 8.7 / 1000  # 8.7 m/s² converted to km/s² (simple approximation)
time_step = 1  # seconds
total_time = 1000  # seconds

# Initial Conditions (adjust these to test different paths)
initial_position = [start_distance, 0]  # x, y in km (starts 6778 km up)
initial_velocity = [0, 7.5]  # km/s (sideways at 7.5 km/s for orbit)

# Lists to store the path
x_positions = [initial_position[0]]
y_positions = [initial_position[1]]
vx = initial_velocity[0]
vy = initial_velocity[1]

# Simulation Loop
for t in range(total_time):
    # Distance to Earth’s center
    r = (x_positions[-1]**2 + y_positions[-1]**2)**0.5
    
    # Gravity pulls toward (0, 0)
    gravity_x = -gravity_constant * x_positions[-1] / r
    gravity_y = -gravity_constant * y_positions[-1] / r
    
    # Update velocity
    vx += gravity_x * time_step
    vy += gravity_y * time_step
    
    # Update position
    new_x = x_positions[-1] + vx * time_step
    new_y = y_positions[-1] + vy * time_step
    
    x_positions.append(new_x)
    y_positions.append(new_y)
    
    # Stop if it hits Earth (optional)
    if r < earth_radius:
        break

# Plotting
plt.figure(figsize=(8, 8))
# Draw Earth
earth_circle = plt.Circle((0, 0), earth_radius, color='blue', alpha=0.3)
plt.gca().add_patch(earth_circle)
# Draw trajectory
plt.plot(x_positions, y_positions, 'r-', label='Payload Path')
plt.plot(0, 0, 'bo', label='Earth Center')  # Earth’s center
plt.axis('equal')  # Equal scaling for x and y
plt.title('Payload Trajectory')
plt.xlabel('X Position (km)')
plt.ylabel('Y Position (km)')
plt.legend()
plt.grid(True)
plt.show()