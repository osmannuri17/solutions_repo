# Problem 2
 # # TASK1 

 Define the first, second, and third cosmic velocities, explaining their physical meaning.

#  First Cosmic Velocity:
Definition: The minimum speed an object needs to orbit a celestial body (like Earth) without falling back down.
Physical Meaning: This is the speed required to become a satellite. For Earth, it’s about 7.9 km/s (around 28,000 km/h). At this speed, the object moves fast enough that its curved path matches the curve of the planet, keeping it in a stable orbit instead of crashing back due to gravity.
# Second Cosmic Velocity:
Definition: The minimum speed an object needs to completely escape a celestial body’s gravitational pull and leave it behind.
Physical Meaning: This is the escape velocity. For Earth, it’s about 11.2 km/s (around 40,000 km/h). At this speed, the object has enough energy to break free from the planet’s gravity and head into space, no longer bound to orbit or return.
# Third Cosmic Velocity:
Definition: The minimum speed an object needs to escape the gravitational pull of a star system (like the Sun) and leave it entirely, starting from a planet within that system.
Physical Meaning: This is about leaving the solar system. For an object starting from Earth, it’s around 16.6 km/s (relative to Earth) when accounting for Earth’s orbit around the Sun. It means the object overcomes both the planet’s and the star’s gravity to travel into interstellar space.
# In short:
First = orbit the planet.
Second = escape the planet.
Third = escape the star system.

 # # TASK2 

 Analyze the mathematical derivations and parameters affecting these velocities.

### **1. First Cosmic Velocity (Orbit Speed)**  
- **What It Is**: Speed to circle a planet without falling.  
- **Simple Math**:  
  - \( v_1 = \sqrt{\frac{G M}{r}} \)  
  - \( G \): Gravity constant (a fixed number).  
  - \( M \): Planet’s mass.  
  - \( r \): Planet’s size (radius).  
- **What Changes It**:  
  - Bigger planet mass (\( M \)): Faster speed needed.  
  - Bigger planet size (\( r \)): Slower speed needed.  
- **Example**: Earth → ~7.9 km/s to orbit.

---

### **2. Second Cosmic Velocity (Escape Speed)**  
- **What It Is**: Speed to leave a planet forever.  
- **Simple Math**:  
  - \( v_2 = \sqrt{\frac{2 G M}{r}} \)  
  - Same \( G \), \( M \), \( r \) as above, just doubled under the square root.  
- **What Changes It**:  
  - Bigger mass (\( M \)): Faster speed.  
  - Bigger size (\( r \)): Slower speed.  
- **Link**: \( v_2 = 1.4 \times v_1 \) (just \( \sqrt{2} \) times orbit speed).  
- **Example**: Earth → ~11.2 km/s to escape.

---

### **3. Third Cosmic Velocity (Star Escape Speed)**  

- **What It Is**: Speed to leave the whole star system (e.g., Sun) from a planet.  
- **Simple Math (Rough)**:
    -  \( v_3 \approx \sqrt{\frac{2 G M_{\text{star}}}{R}} - \text{orbit speed} + v_2 \)  
    - \( M_{\text{star}} \): Star’s mass (like the Sun).  
    - \( R \): Distance from star to planet.  
    - Add planet escape speed (\( v_2 \)).  
- **What Changes It**:  
  - Bigger star mass (\( M_{\text{star}} \)): Faster speed.  
  - Farther from star (\( R \)): Slower speed.  
  - Planet’s mass/size: Affects the starting escape.  
- **Example**: From Earth → ~16.6 km/s to leave the Solar System.

---

### **Super Simple Takeaway**  
- **\( v_1 \)**: Circle the planet → depends on planet’s mass and size.  
- **\( v_2 \)**: Leave the planet → 1.4 times \( v_1 \).  
- **\( v_3 \)**: Leave the star → adds star’s pull and distance.  

Mass pulls harder (faster speed). Distance spreads pull (slower speed). That’s it! Let me know if this works or if you want it even simpler!

#  # TASK3 

 Calculate and visualize these velocities for different celestial bodies like Earth, Mars adn Jupyter.

### **Basic Info for Calculations**  
- I’ll use approximate values for mass (\( M \)) and radius (\( r \)) of each body.  
- For third velocity, I’ll assume escaping the Sun from each planet’s distance (\( R \)), simplified.  
- No heavy math—just results from plugging in numbers!

#### **Earth**  
- Mass: \( 5.97 \times 10^{24} \, kg \)  
- Radius: \( 6,371 \, km \)  
- Distance from Sun: \( 1 \, AU \) (149.6 million km)

#### **Mars**  
- Mass: \( 6.42 \times 10^{23} \, kg \) (about 1/10 Earth’s)  
- Radius: \( 3,390 \, km \) (about half Earth’s)  
- Distance from Sun: \( 1.52 \, AU \) (227 million km)

#### **Jupiter**  
- Mass: \( 1.90 \times 10^{27} \, kg \) (318 times Earth’s)  
- Radius: \( 69,911 \, km \) (11 times Earth’s)  
- Distance from Sun: \( 5.2 \, AU \) (778 million km)

---

### **Calculated Velocities (Simple Results)**  

#### **Earth**  
- **First (Orbit)**: ~7.9 km/s  
- **Second (Escape)**: ~11.2 km/s  
- **Third (Sun Escape)**: ~16.6 km/s (includes escaping Earth + extra to leave Sun)

#### **Mars**  
- **First (Orbit)**: ~3.6 km/s (less mass, smaller size than Earth)  
- **Second (Escape)**: ~5.0 km/s  
- **Third (Sun Escape)**: ~14.3 km/s (farther from Sun, less extra speed needed)

#### **Jupiter**  
- **First (Orbit)**: ~42.1 km/s (huge mass, big size)  
- **Second (Escape)**: ~59.5 km/s  
- **Third (Sun Escape)**: ~18.5 km/s (much farther from Sun, but massive planet escape)

---

### **Why These Numbers?**  
- **First**: Bigger mass = faster, bigger radius = slower. Jupiter’s huge mass wins.  
- **Second**: Same deal, just 1.4 times the first.  
- **Third**: Adds escaping the Sun—closer planets (Earth) need more speed, farther ones (Jupiter) less, but planet escape matters too.

---

### **Simple Visualization**  
Imagine a bar chart (I can’t draw it here, but I’ll describe it):  
- **X-axis**: Three bars for Earth, Mars, Jupiter.  
- **Y-axis**: Speed in km/s (0 to 60 km/s).  
- **Bars**:  
  - **Earth**: Three bars—7.9 (blue), 11.2 (green), 16.6 (red).  
  - **Mars**: Three bars—3.6 (blue), 5.0 (green), 14.3 (red).  
  - **Jupiter**: Three bars—42.1 (blue), 59.5 (green), 18.5 (red).  
- **Colors**: Blue = orbit, Green = escape planet, Red = escape Sun.  
$$
 # Deliverables
$$

# Cosmic Velocities Simulation

This document provides a simple Python script to calculate and visualize the first, second, and third cosmic velocities for Earth, Mars, and Jupiter.

## Python Script

docs/1 Physics/2 Gravity/markdown.py



