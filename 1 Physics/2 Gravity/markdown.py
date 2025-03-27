
import numpy as np
import matplotlib.pyplot as plt

# Constants (in SI units, converted later)
G = 6.674e-11  # m^3 kg^-1 s^-2
AU = 1.496e11  # meters

# Celestial body data (mass in kg, radius in km, distance from Sun in AU)
bodies = {
    "Earth": {"mass": 5.97e24, "radius": 6371, "distance": 1.0},
    "Mars": {"mass": 6.42e23, "radius": 3390, "distance": 1.52},
    "Jupiter": {"mass": 1.90e27, "radius": 69911, "distance": 5.2}
}
sun_mass = 1.989e30  # kg

# Function to calculate velocities (in km/s)
def calculate_velocities(mass, radius, distance_au):
    # Convert radius to meters
    r = radius * 1000
    # First cosmic velocity (orbital)
    v1 = np.sqrt(G * mass / r) / 1000  # Convert m/s to km/s
    # Second cosmic velocity (escape)
    v2 = np.sqrt(2 * G * mass / r) / 1000
    # Third cosmic velocity (simplified: escape Sun from planet's distance)
    R = distance_au * AU  # Distance to Sun in meters
    v_sun_escape = np.sqrt(2 * G * sun_mass / R) / 1000  # Escape Sun at R
    v_orbit = np.sqrt(G * sun_mass / R) / 1000  # Orbital speed around Sun
    v3 = v2 + (v_sun_escape - v_orbit)  # Add extra speed to escape Sun
    return v1, v2, v3

# Calculate velocities for each body
results = {}
for body, data in bodies.items():
    v1, v2, v3 = calculate_velocities(data["mass"], data["radius"], data["distance"])
    results[body] = {"v1": v1, "v2": v2, "v3": v3}

# Print results
for body, velocities in results.items():
    print(f"{body}:")
    print(f"  First (Orbit): {velocities['v1']:.1f} km/s")
    print(f"  Second (Escape): {velocities['v2']:.1f} km/s")
    print(f"  Third (Sun Escape): {velocities['v3']:.1f} km/s")

# Visualization
bodies_list = list(results.keys())
v1_values = [results[body]["v1"] for body in bodies_list]
v2_values = [results[body]["v2"] for body in bodies_list]
v3_values = [results[body]["v3"] for body in bodies_list]

x = np.arange(len(bodies_list))
width = 0.25

plt.bar(x - width, v1_values, width, label="First (Orbit)", color="blue")
plt.bar(x, v2_values, width, label="Second (Escape)", color="green")
plt.bar(x + width, v3_values, width, label="Third (Sun Escape)", color="red")

plt.xlabel("Celestial Bodies")
plt.ylabel("Velocity (km/s)")
plt.title("Cosmic Velocities for Earth, Mars, and Jupiter")
plt.xticks(x, bodies_list)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()