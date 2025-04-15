import numpy as np
import matplotlib.pyplot as plt

g_earth = 9.81
g_moon = 1.62

def get_range(v0, angle_deg, height=0, gravity=g_earth):
    angle_rad = np.radians(angle_deg)
    if height == 0:
        range_dist = (v0 * v0 * np.sin(2 * angle_rad)) / gravity
    else:
        time = (v0 * np.sin(angle_rad) + np.sqrt((v0 * np.sin(angle_rad))**2 + 2 * gravity * height)) / gravity
        range_dist = v0 * np.cos(angle_rad) * time
    return max(range_dist, 0)

def get_range_with_drag(v0, angle_deg, dt=0.01, k=0.1):
    angle_rad = np.radians(angle_deg)
    vx = v0 * np.cos(angle_rad)
    vy = v0 * np.sin(angle_rad)
    x, y = 0, 0
    while y >= 0:
        vx -= k * vx * dt
        vy -= (g_earth + k * vy) * dt
        x += vx * dt
        y += vy * dt
    return max(x, 0)

angles = np.arange(10, 81, 1)
speeds = [10, 20]
heights = [0, 5]

plt.figure(figsize=(10, 6))
for v0 in speeds:
    for h in heights:
        ranges = [get_range(v0, a, h) for a in angles]
        plt.plot(angles, ranges, label=f'Speed={v0} m/s, Height={h} m (Earth)')
    ranges_moon = [get_range(v0, a, 0, g_moon) for a in angles]
    plt.plot(angles, ranges_moon, '--', label=f'Speed={v0} m/s (Moon)')
    ranges_drag = [get_range_with_drag(v0, a) for a in angles]
    plt.plot(angles, ranges_drag, ':', label=f'Speed={v0} m/s (Air drag)')

plt.title('Range vs. Launch Angle')
plt.xlabel('Angle (degrees)')
plt.ylabel('Range (meters)')
plt.grid(True)
plt.legend()
plt.show()