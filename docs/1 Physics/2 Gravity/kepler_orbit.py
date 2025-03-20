import numpy as np

G = 6.674e-11  
M_sun = 1.989e30  
AU = 1.496e11  
def orbital_period(r, M):
    return 2 * np.pi * np.sqrt(r**3 / (G * M))
radii = np.array([1, 2, 3]) * AU  
periods = [orbital_period(r, M_sun) for r in radii]
seconds_per_year = 3.156e7 
periods_years = [p / seconds_per_year for p in periods]
T_squared = [p**2 for p in periods]
r_cubed = [r**3 for r in radii]
constant = [t2 / r3 for t2, r3 in zip(T_squared, r_cubed)]
print("Radius (AU) | Period (years) | T^2/r^3 (s^2/m^3)")
print("------------|---------------|-----------------")
for r, y, c in zip(radii/AU, periods_years, constant):
    print(f"{r:.1f}        | {y:.2f}          | {c:.2e}")
theoretical_constant = 4 * np.pi**2 / (G * M_sun)
print(f"\nTheoretical constant (4π²/GM): {theoretical_constant:.2e} s^2/m^3") 