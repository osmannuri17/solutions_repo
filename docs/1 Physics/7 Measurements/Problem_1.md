# Problem 1


## **Experiment: Measuring the Acceleration Due to Gravity Using a Pendulum**

---

### **1. Objective**

To determine the local gravitational acceleration $g$ using a simple pendulum and to analyze the uncertainties.

---

### **2. Materials**

* String (\~1.0 m)
* Small dense weight (bob)
* Ruler (±0.005 m uncertainty)
* Stopwatch or phone timer

---

### **3. Setup**

* Suspend the pendulum from a fixed point.
* Measure length $L$ from pivot to the **center of the bob**.
* Use small swing angles (<10°) to ensure the formula is valid:

  $$
  T = 2\pi \sqrt{\frac{L}{g}}
  $$

---

### **4. Measurement**

**Pendulum length**:

$$
L = 1.000 \pm 0.005 \, \text{m}
$$

**Time for 10 oscillations (10 trials)**:

| Trial | Time (s) |
| ----- | -------- |
| 1     | 20.1     |
| 2     | 20.2     |
| 3     | 20.0     |
| 4     | 20.1     |
| 5     | 20.3     |
| 6     | 20.2     |
| 7     | 20.1     |
| 8     | 20.2     |
| 9     | 20.0     |
| 10    | 20.1     |

---

### **5. Calculations**

**Mean time for 10 oscillations**:

$$
\overline{T_{10}} = 20.13 \, \text{s}
$$

**Standard deviation**:

$$
\sigma = 0.095 \, \text{s}
$$

**Uncertainty in mean**:

$$
\Delta T_{10} = \frac{0.095}{\sqrt{10}} = 0.030 \, \text{s}
$$

**Period of one oscillation**:

$$
T = \frac{20.13}{10} = 2.013 \, \text{s}
$$

$$
\Delta T = \frac{0.030}{10} = 0.003 \, \text{s}
$$

**Gravitational acceleration**:

$$
g = \frac{4\pi^2 L}{T^2} = \frac{4\pi^2 \cdot 1.000}{(2.013)^2} = 9.74 \, \text{m/s}^2
$$

**Uncertainty in $g$**:

$$
\frac{\Delta g}{g} = \sqrt{ \left( \frac{0.005}{1.000} \right)^2 + \left( 2 \cdot \frac{0.003}{2.013} \right)^2 } = 0.0058
$$

$$
\Delta g = 0.0058 \cdot 9.74 = 0.06 \, \text{m/s}^2
$$

---

### **6. Final Result**

$$
\boxed{g = 9.74 \pm 0.06 \, \text{m/s}^2}
$$

---

### **7. Python Code**

```python
import numpy as np

L = 1.000  
delta_L = 0.005

T10_values = np.array([20.1, 20.2, 20.0, 20.1, 20.3, 20.2, 20.1, 20.2, 20.0, 20.1])

mean_T10 = np.mean(T10_values)
std_T10 = np.std(T10_values, ddof=1)
delta_T10 = std_T10 / np.sqrt(len(T10_values))

T = mean_T10 / 10
delta_T = delta_T10 / 10

g = (4 * np.pi**2 * L) / (T**2)

rel_uncertainty_g = np.sqrt((delta_L / L)**2 + (2 * delta_T / T)**2)
delta_g = rel_uncertainty_g * g

print(f"Mean T10 = {mean_T10:.2f} s")
print(f"Standard deviation = {std_T10:.3f} s")
print(f"Period T = {T:.3f} s ± {delta_T:.4f} s")
print(f"g = {g:.2f} m/s^2 ± {delta_g:.2f} m/s^2")
```

Mean T10 = 20.13 s
Standard deviation = 0.095 s
Period T = 2.013 s ± 0.0030 s
g = 9.74 m/s^2 ± 0.06 m/s^2

---

```python
import numpy as np
L = 1.000 
delta_L = 0.005 
T_10_measurements = np.array([20.10, 20.15, 20.08, 20.12, 20.09]) 
T_10_avg = np.mean(T_10_measurements)
sigma_T = np.std(T_10_measurements, ddof=1)
delta_T_10 = sigma_T / np.sqrt(len(T_10_measurements))
T = T_10_avg / 10
delta_T = delta_T_10 / 10
g = 4 * np.pi**2 * L / (T**2)
relative_delta_g = (delta_L / L) + 2 * (delta_T / T)
delta_g = g * relative_delta_g
print("Tabulated Data:")
print("| Variable        | Value          | Uncertainty      |")
print(f"| \\( L \\)         | {L:.3f} m        | \\( \\Delta L \\) = {delta_L:.3f} m  |")
print(f"| \\( T_{{10}} \\)    | {T_10_avg:.3f} s       | \\( \\Delta T_{{10}} \\) = {delta_T_10:.4f} s |")
print(f"| \\( \\overline{{T}}_{{10}} \\) | {T_10_avg:.3f} s | -                |")
print(f"| \\( \\sigma_T \\)  | {sigma_T:.4f} s       | -                |")
print(f"| \\( T \\)         | {T:.4f} s       | \\( \\Delta T \\) = {delta_T:.4f} s |")
print(f"| \\( g \\)         | {g:.3f} m/s²     | \\( \\Delta g \\) = {delta_g:.3f} m/s² |")
```

### Tabulated Data:
| Variable        | Value          | Uncertainty      |
| \( L \)         | 1.000 m        | \( \Delta L \) = 0.005 m  |
| \( T_{10} \)    | 20.108 s       | \( \Delta T_{10} \) = 0.0124 s |
| \( \overline{T}_{10} \) | 20.108 s | -                |
| \( \sigma_T \)  | 0.0277 s       | -                |
| \( T \)         | 2.0108 s       | \( \Delta T \) = 0.0012 s |
| \( g \)         | 9.764 m/s²     | \( \Delta g \) = 0.061 m/s² |

