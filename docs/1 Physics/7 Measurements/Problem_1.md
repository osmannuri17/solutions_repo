# Problem 1

---

### **Task: Measuring the Acceleration Due to Gravity (g) Using a Pendulum and Analyzing Uncertainties**

---

#### **Objective**

To measure the acceleration due to gravity, $g$, using a simple pendulum, and to conduct a thorough analysis of the uncertainties involved in the measurement.

---

### **1. Theoretical Background**

For a simple pendulum of length $L$ undergoing small amplitude oscillations, the period $T$ of oscillation is given by:

$$
T = 2\pi \sqrt{\frac{L}{g}}
$$

Solving for $g$:

$$
g = \frac{4\pi^2 L}{T^2}
$$

---

### **2. Experimental Procedure**

#### **Materials Needed**

* String
* Small dense bob (e.g., metal sphere)
* Meter stick or ruler
* Stopwatch or digital timer
* Clamp stand or fixed support
* Protractor (optional, to ensure small angles)

#### **Steps**

1. **Set up the pendulum:** Attach the bob to one end of the string and fix the other end to a support.
2. **Measure the length $L$:** Measure from the point of suspension to the center of the bob. Record this with its uncertainty.
3. **Displace and release:** Displace the pendulum by a small angle (less than \~10°) and release it.
4. **Measure the time for $N$ oscillations:** Use a stopwatch to time multiple oscillations (e.g., 20 swings) for better accuracy.
5. **Calculate period $T$:**

   $$
   T = \frac{t_{\text{total}}}{N}
   $$
6. **Repeat the experiment:** Conduct multiple trials to average and reduce random error.

---

### **3. Sample Calculations**

Assume:

* Measured length: $L = 0.800 \pm 0.002 \, \text{m}$
* Time for 20 oscillations: $t = 35.8 \pm 0.2 \, \text{s}$
* Period: $T = \frac{35.8}{20} = 1.790 \, \text{s}$
* Uncertainty in $T$:

  $$
  \Delta T = \frac{0.2}{20} = 0.010 \, \text{s}
  $$

Then:

$$
g = \frac{4\pi^2 \cdot 0.800}{(1.790)^2} \approx 9.86 \, \text{m/s}^2
$$

---

### **4. Uncertainty Analysis**

#### **Uncertainty in g**

Using error propagation:

$$
\frac{\Delta g}{g} = \sqrt{ \left( \frac{\Delta L}{L} \right)^2 + \left( 2 \cdot \frac{\Delta T}{T} \right)^2 }
$$

Substitute values:

$$
\frac{\Delta g}{g} = \sqrt{ \left( \frac{0.002}{0.800} \right)^2 + \left( 2 \cdot \frac{0.010}{1.790} \right)^2 } \approx 0.0118
$$

$$
\Delta g = 0.0118 \cdot 9.86 \approx 0.12 \, \text{m/s}^2
$$

$$
\boxed{g = 9.86 \pm 0.12 \, \text{m/s}^2}
$$

---

### **5. Discussion**

* **Accuracy**: The measured value is close to the standard $9.81 \, \text{m/s}^2$, indicating good accuracy.

* **Sources of Uncertainty**:

  * Human reaction time in stopwatch use (\~0.2 s typical)
  * Uncertainty in length measurement (e.g., due to bob center approximation)
  * Air resistance and pivot friction (neglected here)
  * Angle of release (nonlinearities for large angles)

* **Improvement Suggestions**:

  * Use a photogate timer for precise period measurement.
  * Ensure more trials and better length calibration.
  * Minimize amplitude to stay within the small-angle approximation.

---

### **Conclusion**

By carefully measuring the period of a simple pendulum and analyzing uncertainties, we determined the local gravitational acceleration to be:

$$
\boxed{g = 9.86 \pm 0.12 \, \text{m/s}^2}
$$

This exercise demonstrates the importance of precision and uncertainty analysis in experimental physics.

---



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

