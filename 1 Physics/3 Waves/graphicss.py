import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

r1 = np.sqrt((X + 2)**2 + Y**2)
r2 = np.sqrt((X - 2)**2 + Y**2)

wavelength = 2  
k = 2 * np.pi / wavelength  
wave1 = np.sin(k * r1)
wave2 = np.sin(k * r2)

interference = wave1 + wave2  

plt.figure(figsize=(8,6))
plt.contourf(X, Y, interference, levels=50, cmap='coolwarm')
plt.colorbar(label="Wave Amplitude")
plt.title("Constructive & Destructive Interference")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
