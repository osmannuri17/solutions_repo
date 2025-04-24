# Problem 2

# Theoretical Foundation:

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
