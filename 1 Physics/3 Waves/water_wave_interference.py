import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1.0  # Amplitude
wavelength = 0.5  # Wavelength
k = 2 * np.pi / wavelength  # Wave number
f = 1.0  # Frequency
omega = 2 * np.pi * f  # Angular frequency
t = 0.0  # Time (snapshot at t=0)
d = 1.0  # Side length of the equilateral triangle

# Positions of the sources (vertices of an equilateral triangle)
# Centered at the origin
h = d / np.sqrt(3)  # Height of the triangle for positioning
sources = [
    (0, h),              # Top vertex
    (-d/2, -h/2),        # Bottom-left vertex
    (d/2, -h/2)          # Bottom-right vertex
]

# Create a grid of points
x = np.linspace(-2, 2, 100)  # x-range
y = np.linspace(-2, 2, 100)  # y-range
X, Y = np.meshgrid(x, y)  # 2D grid

# Initialize the total displacement
eta_total = np.zeros_like(X)

# Compute the wave contribution from each source
for (x0, y0) in sources:
    # Distance from the source to each point on the grid
    r = np.sqrt((X - x0)**2 + (Y - y0)**2)
    # Avoid division by zero at the source
    r = np.maximum(r, 1e-10)
    # Wave displacement from this source
    eta = (A / np.sqrt(r)) * np.cos(k * r - omega * t)
    # Add to the total displacement (superposition)
    eta_total += eta

# Plot the interference pattern
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, eta_total, cmap='seismic', levels=50)
plt.colorbar(label='Wave Displacement')
plt.scatter([s[0] for s in sources], [s[1] for s in sources], 
            color='black', marker='o', label='Sources')
plt.title('Interference Pattern from Three Sources (Equilateral Triangle)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Equal aspect ratio for better visualization
plt.show()