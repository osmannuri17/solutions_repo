# Problem 2

# Define velocities:

***First Cosmic Velocity (Orbital Velocity):***

The speed to orbit a celestial body without falling back. Gravity pulls it down, but its speed keeps it moving forward, resulting in a continuous circle.


1.  **Gravity equals centripetal force:** 

For a stable low orbit, the gravitational force ($G \frac{Mm}{R^2}$) equals the centripetal force ($m \frac{v_1^2}{R}$).

2.  **Equation:**

    $$G \frac{Mm}{R^2} = m \frac{v_1^2}{R}$$

3.  **Solve for $v_1$:**
    * Cancel $m$:  $G \frac{M}{R^2} = \frac{v_1^2}{R}$
    * Multiply by $R$: $G \frac{M}{R} = v_1^2$
    * Take square root: $v_1 = \sqrt{\frac{GM}{R}}$

4.  **Using surface gravity ($g = \frac{GM}{R^2}$):**

    $v_1 = \sqrt{\frac{GM}{R}} = \sqrt{\frac{GM}{R^2} \cdot R} = \sqrt{gR}$

**Formula for First Cosmic Velocity:**

$$v_1 = \sqrt{\frac{GM}{R}} \quad \text{or} \quad v_1 = \sqrt{gR}$$

***Second Cosmic Velocity (Escape Velocity):***

The speed to break free from a celestial body's gravity completely and never return. It's the point where the object has enough energy to overcome the gravitational pull.

1.  **Conservation of Energy:**

 For an object to escape the gravitational pull of a celestial body, its initial kinetic energy must be at least equal to the magnitude of its initial gravitational potential energy.

2.  **Energy Equation:**
    $$\frac{1}{2} m v_2^2 - G \frac{Mm}{R} = 0$$
    where:
    * $v_2$ is the second cosmic velocity.
    * $m$ is the mass of the escaping object.
    * $M$ is the mass of the celestial body.
    * $R$ is the distance from the center of the celestial body (typically its radius when launching from the surface).
    * $G$ is the universal gravitational constant.

3.  **Solve for $v_2$:**
    * Move the potential energy term to the right side:
        $$\frac{1}{2} m v_2^2 = G \frac{Mm}{R}$$
    * Cancel out the mass of the escaping object ($m$):
        $$\frac{1}{2} v_2^2 = G \frac{M}{R}$$
    * Multiply by 2:
        $$v_2^2 = 2 G \frac{M}{R}$$
    * Take the square root:
        $$v_2 = \sqrt{\frac{2GM}{R}}$$

4.  **Using surface gravity ($g = \frac{GM}{R^2}$):**

    $$v_2 = \sqrt{2 \cdot \frac{GM}{R} \cdot \frac{R}{R}} = \sqrt{2 \cdot \frac{GM}{R^2} \cdot R} = \sqrt{2gR}$$

**Formula for Second Cosmic Velocity:**

$$v_2 = \sqrt{\frac{2GM}{R}} \quad \text{or} \quad v_2 = \sqrt{2gR}$$


***Third Cosmic Velocity (Solar System Escape Velocity):***
The speed needed, when launching from Earth, to escape the Sun's gravity and leave the entire solar system. It's about overcoming the Sun's pull while already moving with Earth.

 The generally accepted value is approximately 16.7 km/s.


# Analyzing mathematical derivations of velocities:

### First Cosmic Velocity (Orbital Velocity)

* **Simplified Derivation:**

 For a stable circular orbit, the gravitational force pulling the object towards the center of the celestial body must equal the centripetal force needed to keep it moving in a circle.
    $$\frac{GMm}{r^2} = \frac{mv_1^2}{r}$$
    Where:
    * \(G\) is the universal gravitational constant.
    * \(M\) is the mass of the celestial body.
    * \(m\) is the mass of the orbiting object (which cancels out).
    * \(r\) is the radius of the orbit (approximately the radius of the celestial body if orbiting just above the surface).
    * \(v_1\) is the first cosmic velocity.

    Solving for \(v_1\), we get:
    $$v_1 = \sqrt{\frac{GM}{r}}$$

* **Parameters Affecting \(v_1\):**
    * **Mass of the Celestial Body (\(M\)):** A more massive body exerts a stronger gravitational pull, requiring a higher orbital velocity to maintain a stable orbit. \(v_1\) is directly proportional to the square root of \(M\).
    * **Radius of the Orbit (\(r\)):** The closer the orbit is to the center of the celestial body (smaller \(r\)), the stronger the gravitational force and the higher the required orbital velocity. \(v_1\) is inversely proportional to the square root of \(r\).

### Second Cosmic Velocity (Escape Velocity)

* **Simplified Derivation:** Escape velocity is achieved when the kinetic energy of an object is equal to the magnitude of its gravitational potential energy.
    $$\frac{1}{2}mv_e^2 = \frac{GMm}{r}$$
    Where:
    * \(G\) is the universal gravitational constant.
    * \(M\) is the mass of the celestial body.
    * \(m\) is the mass of the escaping object (which cancels out).
    * \(r\) is the initial distance from the center of the celestial body (typically its radius).
    * \(v_e\) is the escape velocity.

Solving for \(v_e\), we get:
    $$v_e = \sqrt{\frac{2GM}{r}}$$

 Notice that \(v_e = \sqrt{2} \cdot v_1\).

* **Parameters Affecting \(v_e\):**

 * **Mass of the Celestial Body (\(M\)):**

Similar to orbital velocity, a more massive body has a stronger gravitational pull, requiring a higher escape velocity. \(v_e\) is directly proportional to the square root of \(M\).

 * **Initial Distance from the Center (\(r\)):**

 The closer the object starts to the center (smaller \(r\)), the stronger the gravitational pull it needs to overcome, resulting in a higher escape velocity. \(v_e\) is inversely proportional to the square root of \(r\).

### Third Cosmic Velocity (Solar System Escape Velocity from Earth's Orbit)

* **Simplified Explanation of Parameters:**

 The third cosmic velocity is more complex as it involves escaping the gravitational influence of both Earth and the Sun.
 It depends on:
    * **Sun's Mass:**

 The primary factor determining the overall escape speed from the solar system at Earth's orbital distance.
 * **Earth's Orbital Velocity:**

Earth is already moving around the Sun at a significant speed. Launching in the direction of Earth's motion allows us to use this existing velocity as part of the escape velocity.

* **Earth's Mass and Radius:**

 These determine the escape velocity from Earth's surface, which is the initial "push" needed to get away from our planet's gravity before focusing on escaping the Sun.

* **Launch Trajectory:**

The direction of the initial velocity relative to Earth's orbital motion around the Sun significantly affects the required speed. Launching in Earth's direction of travel is most efficient.

* **Approximate Calculation (Conceptual):**
    1.  Calculate the escape velocity from the Sun's gravity at Earth's orbital distance.
    2.  Consider Earth's orbital velocity around the Sun.
    3.  The third cosmic velocity is roughly the speed needed (relative to Earth) so that the vector sum of this speed and Earth's orbital velocity equals the escape velocity from the Sun.

 We also need to account for escaping Earth's gravity initially.

The precise mathematical derivation involves energy conservation in both gravitational fields and is more involved than the first two cosmic velocities. The commonly cited value of approximately 16.7 km/s relative to Earth is the result of these more complex calculations and takes into account an optimal launch trajectory.

```python
import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11

celestial_bodies_data = [
    {"name": "Earth", "mass": 5.972e24, "radius": 6.371e6, "color": "blue"},
    {"name": "Mars", "mass": 6.39e23, "radius": 3.390e6, "color": "red"},
    {"name": "Jupiter", "mass": 1.898e27, "radius": 6.9911e7, "color": "orange"},
]

def calculate_escape_velocity(mass, radius):
    return np.sqrt((2 * G * mass) / radius) / 1000

def calculate_orbital_velocity(mass, radius):
    return np.sqrt((G * mass) / radius) / 1000

for body in celestial_bodies_data:
    body["escape_velocity"] = calculate_escape_velocity(body["mass"], body["radius"])
    body["orbital_velocity"] = calculate_orbital_velocity(body["mass"], body["radius"])

print("Calculated Escape and Orbital Velocities (km/s):")
for body in celestial_bodies_data:
    print(f"{body['name']}:")
    print(f"  Escape Velocity: {body['escape_velocity']:.2f} km/s")
    print(f"  Orbital Velocity: {body['orbital_velocity']:.2f} km/s")
    print("-" * 20)

body_names = [body["name"] for body in celestial_bodies_data]
escape_velocities = [body["escape_velocity"] for body in celestial_bodies_data]
orbital_velocities = [body["orbital_velocity"] for body in celestial_bodies_data]
colors = [body["color"] for body in celestial_bodies_data]

plt.figure(figsize=(8, 5))
plt.bar(body_names, escape_velocities, color=colors)
plt.ylabel("Escape Velocity (km/s)")
plt.title("Escape Velocities of Earth, Mars, and Jupiter")
plt.grid(axis='y', linestyle='--')
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(body_names, orbital_velocities, color=colors)
plt.ylabel("Orbital Velocity (km/s)")
plt.title("Orbital Velocities (at Surface) of Earth, Mars, and Jupiter")
plt.grid(axis='y', linestyle='--')
plt.show()

x = np.arange(len(body_names))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, escape_velocities, width, label='Escape Velocity', color=colors)
rects2 = ax.bar(x + width/2, orbital_velocities, width, label='Orbital Velocity', color=colors, alpha=0.6)

ax.set_ylabel('Velocity (km/s)')
ax.set_title('Comparison of Escape and Orbital Velocities')
ax.set_xticks(x)
ax.set_xticklabels(body_names)
ax.legend()
ax.grid(axis='y', linestyle='--')

fig.tight_layout()
plt.show()

print("\nNote: The third cosmic velocity is specific to escaping the solar system from Earth and is not directly calculated or visualized here for individual planets.")
```

![alt text](Figure_1.png)

![alt text](Figure_2.png)

![alt text](Figure_3.png) 


# Cosmic velocities are crucial for space exploration:

***First Cosmic Velocity (Orbital):***

The speed needed to put satellites into orbit around a planet. Essential for communication,observation, etc.

***Second Cosmic Velocity (Escape):***

The speed to leave a planet's gravity, necessary for interplanetary travel (e.g., missions to Mars).

***Third Cosmic Velocity (Solar System Escape):***

The speed to exit our solar system, a requirement for future interstellar travel.

**These velocities dictate the energy needed for different space missions and are fundamental for planning and achieving space exploration goals.**


# Graphical representations of escape velocities and cosmic velocities for various celestial bodies.

```python
import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11

celestial_bodies_data = [
    {"name": "Earth", "mass": 5.972e24, "radius": 6.371e6, "color": "blue"},
    {"name": "Mars", "mass": 6.39e23, "radius": 3.390e6, "color": "red"},
    {"name": "Jupiter", "mass": 1.898e27, "radius": 6.9911e7, "color": "orange"},
    {"name": "Moon", "mass": 7.348e22, "radius": 1.737e6, "color": "gray"},
    {"name": "Sun", "mass": 1.989e30, "radius": 6.957e8, "color": "yellow"},
]

def calculate_escape_velocity(mass, radius):
    return np.sqrt((2 * G * mass) / radius) / 1000

def calculate_orbital_velocity(mass, radius):
    return np.sqrt((G * mass) / radius) / 1000

for body in celestial_bodies_data:
    body["escape_velocity"] = calculate_escape_velocity(body["mass"], body["radius"])
    body["orbital_velocity"] = calculate_orbital_velocity(body["mass"], body["radius"])

body_names = [body["name"] for body in celestial_bodies_data]
escape_velocities = [body["escape_velocity"] for body in celestial_bodies_data]
orbital_velocities = [body["orbital_velocity"] for body in celestial_bodies_data]
colors = [body["color"] for body in celestial_bodies_data]

plt.figure(figsize=(10, 6))
plt.bar(body_names, escape_velocities, color=colors)
plt.ylabel("Escape Velocity (km/s)")
plt.title("Escape Velocities of Various Celestial Bodies")
plt.grid(axis='y', linestyle='--')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(body_names, orbital_velocities, color=colors)
plt.ylabel("Orbital Velocity (km/s)")
plt.title("Orbital Velocities (at Surface) of Various Celestial Bodies")
plt.grid(axis='y', linestyle='--')
plt.show()

x = np.arange(len(body_names))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))
rects1 = ax.bar(x - width/2, escape_velocities, width, label='Escape Velocity', color=colors)
rects2 = ax.bar(x + width/2, orbital_velocities, width, label='Orbital Velocity', color=colors, alpha=0.6)

ax.set_ylabel('Velocity (km/s)')
ax.set_title('Comparison of Escape and Orbital Velocities')
ax.set_xticks(x)
ax.set_xticklabels(body_names)
ax.legend()
ax.grid(axis='y', linestyle='--')
fig.tight_layout()
plt.show()
```

![alt text](Figure_1-1.png)

![alt text](<Figure_2 kopyası.png>)

![alt text](Figure_3-1.png) 




