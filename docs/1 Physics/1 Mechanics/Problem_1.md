# Problem 1

# Theoretical Foundation

Projectile motion starts with two simple ideas: horizontally, a projectile moves at a steady speed because nothing pushes it side-to-side; vertically, gravity pulls it down at a constant rate (9.81 m/s² on Earth). These rules create a curved path, like throwing a ball. The path changes based on:

***Speed:*** 
Throw faster, it goes farther and higher.

***Angle:***
 Low angles favor distance; high angles give height.

***Starting height:*** 
Throwing from higher up extends the flight.

***Gravity:*** 
Weaker gravity (like the Moon’s) stretches the path
.
This creates a “family” of paths—each mix of speed, angle, height, or gravity gives a unique curve. For example, a hard throw at 45°
 travels far, while a soft throw straight up lands close. These variations fit many scenarios, from sports to space launches.


# Analysis of the Range

The range (how far the projectile lands) depends heavily on the launch angle:

***Best angle:*** Around 45° usually gives the farthest range on flat ground, balancing height and distance.

***Symmetry:*** Angles like 30° and 60° give the same range, but less than 45°.

***No range:*** Throwing straight up (90°) or flat (0°) means it doesn’t go anywhere horizontally.

### Other factors affect the range too:

***Speed:*** A faster throw (e.g., 20 m/s vs. 10 m/s) sends it much farther.

***Gravity:*** On the Moon (gravity = 1.62 m/s²), the range is way longer than on Earth.

***Starting height:*** Throwing from a height (e.g., 5 m up) adds distance because it stays in the air longer.

For example, a 20 m/s throw at 45° goes farther than a 10 m/s throw, and even farther if launched from a hill or on the Moon.


# Practical Applications

This model applies to real-world situations but needs tweaks for accuracy:

***Uneven terrain:***
 On a hill, the landing spot shifts. A downhill slope might increase range, like a golf ball rolling farther.

***Air resistance:*** 
Air slows the projectile, shortening the range. The best angle drops to maybe 35°–40°, as seen in sports like baseball.

### Examples:

***Sports:*** 
In soccer, a well-angled kick clears defenders and reaches the goal. Golfers aim for distance with similar angle choices.

***Engineering:*** Cannons use these ideas but adjust for wind or hills to hit targets.

***Space:*** On Mars or the Moon, lower gravity means rovers or probes travel farther, helping plan landings.

To make it realistic, we can add air resistance or terrain shapes, often using numerical simulations to handle complex effects, as shown in the script below.

import numpy as np
import matplotlib.pyplot as plt

# Settings
g_earth = 9.81  # Gravity on Earth (m/s^2)
g_moon = 1.62   # Gravity on Moon (m/s^2)

def get_range(v0, angle_deg, height=0, gravity=g_earth):
    """Find how far the projectile goes."""
    angle_rad = np.radians(angle_deg)
    if height == 0:
        range_dist = (v0 * v0 * np.sin(2 * angle_rad)) / gravity
    else:
        time = (v0 * np.sin(angle_rad) + np.sqrt((v0 * np.sin(angle_rad))**2 + 2 * gravity * height)) / gravity
        range_dist = v0 * np.cos(angle_rad) * time
    return max(range_dist, 0)

def get_range_with_drag(v0, angle_deg, dt=0.01, k=0.1):
    """Simulate with air slowing it down."""
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

# Test cases
angles = np.arange(10, 81, 1)  # Angles from 10° to 80°
speeds = [10, 20]  # Speeds in m/s
heights = [0, 5]   # Heights in m

# Plot
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