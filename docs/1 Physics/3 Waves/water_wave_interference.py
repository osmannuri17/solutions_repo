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

h = d / np.sqrt(3)  # Height of the triangle for positioning
sources = [
    (0, h),              # Top vertex
    (-d/2, -h/2),        # Bottom-left vertex
    (d/2, -h/2)          # Bottom-right vertex
]


x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100) 
X, Y = np.meshgrid(x, y) 

eta_total = np.zeros_like(X)
for (x0, y0) in sources:
    r = np.sqrt((X - x0)**2 + (Y - y0)**2)
    r = np.maximum(r, 1e-10)
    eta = (A / np.sqrt(r)) * np.cos(k * r - omega * t)
   
    eta_total += eta

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
plt.axis('equal')
plt.show()