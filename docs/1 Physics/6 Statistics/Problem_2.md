# Problem 2

# PART 1

## Theoretical Foundation:

Great, thanks for sharing the first task. Here's the response based on it:

---

### **1. Theoretical Foundation**

#### **• Explanation: Using the Ratio to Estimate π**

To estimate π using the Monte Carlo method, consider a square enclosing a circle:

- Imagine a **unit circle** (radius = 1) centered at the origin (0, 0).
- This circle fits perfectly inside a square that spans from (-1, -1) to (1, 1), so the square has a side length of 2 and an area of 4.
- Random points are uniformly generated inside this square.

The key idea is to calculate the ratio of points that fall **inside** the circle to the total number of points in the square:

- A point \((x, y)\) lies **inside** the unit circle if \(x^2 + y^2 \leq 1\).

- The probability of a point landing inside the circle is equal to the ratio of the **area of the circle** to the **area of the square**:

  \[
  \text{Probability} = \frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi \cdot 1^2}{4} = \frac{\pi}{4}
  \]

#### **• Derivation of Formula**

Let \(N\) be the total number of random points, and \(N_{\text{in}}\) be the number of points inside the circle.

Using the ratio:

\[
\frac{N_{\text{in}}}{N} \approx \frac{\pi}{4}
\]

Multiply both sides by 4 to estimate π:

\[
\pi \approx 4 \cdot \left( \frac{N_{\text{in}}}{N} \right)
\]


# Simulation

```python
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(num_points):
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)
    inside_circle = (x**2 + y**2) <= 1
    num_inside = np.sum(inside_circle)
    pi_estimate = 4 * num_inside / num_points
    
    return pi_estimate, x, y, inside_circle
point_counts = [100, 1000, 10000, 100000]
pi_estimates = []
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

for num_points in point_counts:
    pi_approx, x, y, inside_circle = monte_carlo_pi(num_points)
    pi_estimates.append(pi_approx)
    if num_points == point_counts[-1]:
        ax1.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
        ax1.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
        ax1.set_aspect('equal')
        ax1.set_title(f'Monte Carlo Simulation\n{num_points} Points')
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.legend()
ax2.plot(point_counts, pi_estimates, marker='o', label='Estimated π')
ax2.axhline(y=np.pi, color='r', linestyle='--', label='Actual π')
ax2.set_xscale('log')
ax2.set_title('Convergence of π Estimate')
ax2.set_xlabel('Number of Points (log scale)')
ax2.set_ylabel('Estimated π')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('monte_carlo_pi_simulation.png')
plt.show()
for num_points, pi_approx in zip(point_counts, pi_estimates):
    print(f"Number of points: {num_points}, Estimated π: {pi_approx:.5f}, Error: {abs(pi_approx - np.pi):.5f}")
```

![alt text](<Unknown kopyası.png>)


- The square spans from \(-1\) to \(1\) in both x and y directions.
- We use a random number generator (e.g., NumPy's `np.random.uniform`) to generate coordinates \((x, y)\) such that:
  \[
  x \in [-1, 1],\quad y \in [-1, 1]
  \]

#### **• Step 2: Count the Points Inside the Circle**

- A point lies **inside** the unit circle if it satisfies the condition:
  \[
  x^2 + y^2 \leq 1
  \]

- Count how many of the randomly generated points satisfy this condition.

#### **• Step 3: Estimate π**

Using the formula derived earlier:

\[
\pi \approx 4 \cdot \left( \frac{\text{Number of points inside the circle}}{\text{Total number of points}} \right)
\]

This ratio approximates π because the area of the unit circle is π, and the area of the square is 4.

The proportion of points falling inside the circle mirrors the ratio of these areas.








