# Problem 1
# Task 1 
Let’s derive Kepler’s Third Law for circular orbits in a simpler way, focusing on the key ideas with less algebra.

Imagine a planet orbiting a star with mass \( M \) in a circle. The orbital radius is \( r \), and the orbital period is \( T \), the time for one full trip around. Two forces are at play: gravity pulls the planet toward the star, and the planet’s circular motion needs a force to keep it from flying off. Gravity provides that force.

Gravity’s strength is:

\[ F_g = \frac{G M m}{r^2} \]

where \( m \) is the planet’s mass and \( G \) is the gravitational constant. For circular motion, the centripetal force depends on speed \( v \) and radius \( r \):

\[ F_c = \frac{m v^2}{r} \]

Since gravity is the centripetal force, they’re equal:

\[ \frac{G M m}{r^2} = \frac{m v^2}{r} \]

Cancel \( m \) (it’s not zero) and simplify:

\[ \frac{G M}{r^2} = \frac{v^2}{r} \]

Multiply both sides by \( r \):

\[ v^2 = \frac{G M}{r} \]

Now, the speed \( v \) is how fast the planet moves around the circle. One orbit’s distance is the circumference, \( 2\pi r \), and it takes time \( T \), so:

\[ v = \frac{2\pi r}{T} \]

Square it:

\[ v^2 = \frac{4\pi^2 r^2}{T^2} \]

Set the two expressions for \( v^2 \) equal:

\[ \frac{4\pi^2 r^2}{T^2} = \frac{G M}{r} \]

Multiply both sides by \( T^2 \) and divide by \( \frac{G M}{r} \) (or cross-multiply):

\[ 4\pi^2 r^2 = \frac{G M}{r} \cdot T^2 \]

Multiply both sides by \( r \):

\[ 4\pi^2 r^3 = G M T^2 \]

Divide by \( G M \):

\[ T^2 = \frac{4\pi^2}{G M} r^3 \]

That’s it! \( T^2 \) (the period squared) is proportional to \( r^3 \) (the radius cubed), with \( \frac{4\pi^2}{G M} \) as the constant. This is Kepler’s Third Law, simplified: 

\[ T^2 \propto r^3 \]
# TASK 2

Let’s discuss the implications of Kepler’s Third Law—the relationship where the square of the orbital period (\( T^2 \)) is proportional to the cube of the orbital radius (\( r^3 \))—for astronomy, focusing on how it helps calculate planetary masses and distances. I’ll keep it simple and straightforward.

### Implications for Astronomy
Kepler’s Third Law, \( T^2 = \frac{4\pi^2}{G M} r^3 \), connects a planet’s orbit to the mass of the object it orbits (like a star or planet) and the distance between them. This is a big deal because it lets astronomers figure out things about space without needing to visit planets or stars. It’s like a cosmic ruler and scale rolled into one.

#### 1. Calculating Planetary Masses
If something (like a moon or satellite) orbits a planet, we can use the law to find the planet’s mass. Here’s how:
- Measure the orbital period \( T \) (how long one orbit takes) and the radius \( r \) (distance from the planet’s center).
- Plug those into the equation: \( T^2 = \frac{4\pi^2}{G M} r^3 \).
- Rearrange to solve for \( M \) (the planet’s mass): \( M = \frac{4\pi^2 r^3}{G T^2} \).
- Since \( G \) is a known constant (\( 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} \)), and we can observe \( T \) and \( r \), we calculate \( M \).

For example, Earth’s moon orbits in about 27.3 days (\( T \)) at a distance of roughly 384,000 km (\( r \)). Using these, astronomers calculated Earth’s mass long ago. The same trick works for any planet with a moon or for the Sun with planets orbiting it.

#### 2. Measuring Distances
If we know the mass of the central body (like the Sun), we can flip the law to find distances:
- Measure \( T \) (say, a planet’s year).
- Use the Sun’s known mass (\( M \approx 1.989 \times 10^{30} \, \text{kg} \)) and solve for \( r \): \( r^3 = \frac{G M T^2}{4\pi^2} \), then take the cube root.
- This gives the average distance from the Sun to the planet.

For instance, if we know Mars takes 687 days to orbit the Sun, we can compute its distance from the Sun using the Sun’s mass. This helped map our solar system before telescopes got super precise.

#### 3. Broader Impact
- **Solar System Design**: The law shows why inner planets (like Mercury) orbit fast and outer ones (like Neptune) take longer—bigger \( r \) means bigger \( T \).
- **Exoplanets**: Astronomers spot planets around other stars by watching how long they take to orbit (\( T \)) and estimating their distance (\( r \)), then guessing the star’s mass.
- **Satellites**: We use it to place satellites at the right distance from Earth for specific orbit times, like 24 hours for GPS satellites.

### Simple Takeaway
Kepler’s Third Law is a tool that turns time and distance into mass and vice versa. Watch how long something orbits and how far it is, and you can weigh a planet or measure its distance from a star. It’s a simple rule that unlocks the scale of the universe!

# TASK 3 
Let’s analyze real-world examples of Kepler’s Third Law (\( T^2 = \frac{4\pi^2}{G M} r^3 \)) using the Moon’s orbit around Earth and the orbits of planets in the Solar System. I’ll keep it simple and based on the given information about orbital period and radius.

### 1. The Moon’s Orbit Around Earth
The Moon orbits Earth, so Earth’s mass (\( M \)) is the central mass in the equation. We can use Kepler’s Third Law to check how the Moon’s orbital period and radius fit together.

- **Orbital Period (\( T \))**: The Moon takes about 27.3 days to orbit Earth. Convert that to seconds for consistency:  
  \( T = 27.3 \, \text{days} \times 86,400 \, \text{s/day} \approx 2.36 \times 10^6 \, \text{seconds} \).
- **Orbital Radius (\( r \))**: The average distance from Earth to the Moon is about 384,000 km, or \( r = 3.84 \times 10^8 \, \text{meters} \).
- **Earth’s Mass (\( M \))**: Known to be about \( 5.972 \times 10^{24} \, \text{kg} \).
- **Gravitational Constant (\( G \))**: \( 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} \).

Plug these into Kepler’s Third Law:  
\[ T^2 = \frac{4\pi^2}{G M} r^3 \]

First, calculate the right side:  
- \( 4\pi^2 \approx 39.478 \),  
- \( G M = (6.674 \times 10^{-11}) \times (5.972 \times 10^{24}) \approx 3.986 \times 10^{14} \, \text{m}^3 \text{s}^{-2} \),  
- \( r^3 = (3.84 \times 10^8)^3 \approx 5.66 \times 10^{25} \, \text{m}^3 \),  
- \( \frac{4\pi^2}{G M} \approx \frac{39.478}{3.986 \times 10^{14}} \approx 9.91 \times 10^{-14} \, \text{s}^2 \text{m}^{-3} \),  
- \( T^2 \approx (9.91 \times 10^{-14}) \times (5.66 \times 10^{25}) \approx 5.61 \times 10^{12} \, \text{s}^2 \).

Now the left side:  
\[ T^2 = (2.36 \times 10^6)^2 \approx 5.57 \times 10^{12} \, \text{s}^2 \].

These numbers match closely (5.57 vs. 5.61), showing Kepler’s Third Law holds for the Moon. The slight difference comes from rounding and the Moon’s slightly elliptical orbit, but for a simple circular model, it works!

### 2. Planets in the Solar System
Now let’s look at planets orbiting the Sun, with the Sun’s mass (\( M \approx 1.989 \times 10^{30} \, \text{kg} \)) as the central mass. We’ll test Earth and Mars.

- **Earth**:  
  - \( T = 1 \, \text{year} \approx 3.156 \times 10^7 \, \text{seconds} \),  
  - \( r = 1 \, \text{AU} \approx 1.496 \times 10^{11} \, \text{meters} \).  
  - \( r^3 = (1.496 \times 10^{11})^3 \approx 3.347 \times 10^{33} \, \text{m}^3 \),  
  - \( G M = (6.674 \times 10^{-11}) \times (1.989 \times 10^{30}) \approx 1.327 \times 10^{20} \, \text{m}^3 \text{s}^{-2} \),  
  - \( \frac{4\pi^2}{G M} \approx \frac{39.478}{1.327 \times 10^{20}} \approx 2.975 \times 10^{-19} \, \text{s}^2 \text{m}^{-3} \),  
  - \( T^2 \approx (2.975 \times 10^{-19}) \times (3.347 \times 10^{33}) \approx 9.96 \times 10^{14} \, \text{s}^2 \),  
  - Actual \( T^2 = (3.156 \times 10^7)^2 \approx 9.96 \times 10^{14} \, \text{s}^2 \).  
  Perfect match!

- **Mars**:  
  - \( T = 687 \, \text{days} \approx 5.94 \times 10^7 \, \text{seconds} \),  
  - \( r = 1.524 \, \text{AU} \approx 2.279 \times 10^{11} \, \text{meters} \),  
  - \( r^3 = (2.279 \times 10^{11})^3 \approx 1.183 \times 10^{34} \, \text{m}^3 \),  
  - \( T^2 \approx (2.975 \times 10^{-19}) \times (1.183 \times 10^{34}) \approx 3.52 \times 10^{15} \, \text{s}^2 \),  
  - Actual \( T^2 = (5.94 \times 10^7)^2 \approx 3.53 \times 10^{15} \, \text{s}^2 \).  
  Another close fit!

### Simple Solution
Kepler’s Third Law works in the real world. For the Moon, its 27.3-day orbit at 384,000 km fits Earth’s mass. For planets like Earth (1 year, 1 AU) and Mars (687 days, 1.524 AU), their orbits match the Sun’s mass. The law ties \( T^2 \) to \( r^3 \), letting us predict and check how things move in space. It’s a simple rule that fits the Moon and planets perfectly!
# TASK 4 
Let’s implement a simple computational model to simulate circular orbits and verify Kepler’s Third Law (\( T^2 = \frac{4\pi^2}{G M} r^3 \)), based on the given information about orbital period and radius. I’ll keep it straightforward, using a basic approach you could code in something like Python, and focus on verifying the relationship.

### Simple Computational Model
We’ll simulate a planet orbiting a star (like the Sun) in a circular orbit. The idea is to calculate the orbital period (\( T \)) for a given radius (\( r \)) and mass (\( M \)), then check if \( T^2 \propto r^3 \) holds. Here’s how to do it simply:

#### Step 1: Set Up the System
- **Central Mass (\( M \))**: Use the Sun’s mass, \( M = 1.989 \times 10^{30} \, \text{kg} \).
- **Gravitational Constant (\( G \))**: \( G = 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2} \).
- **Orbital Radii (\( r \))**: Pick a few distances, like 1 AU, 2 AU, and 3 AU (1 AU = \( 1.496 \times 10^{11} \, \text{m} \)).

#### Step 2: Calculate Orbital Speed
For a circular orbit, the gravitational force equals the centripetal force. The orbital speed (\( v \)) is:
\[ v = \sqrt{\frac{G M}{r}} \]
We’ll compute this for each radius.

#### Step 3: Compute Orbital Period
The period (\( T \)) is the time to travel the circumference (\( 2\pi r \)) at speed \( v \):
\[ T = \frac{2\pi r}{v} = \frac{2\pi r}{\sqrt{\frac{G M}{r}}} \]
Simplify:
\[ T = 2\pi \sqrt{\frac{r^3}{G M}} \]
This matches Kepler’s Third Law when squared: \( T^2 = \frac{4\pi^2}{G M} r^3 \).

#### Step 4: Simulate and Verify
Let’s calculate \( T \) for a few radii, then check \( T^2 \) vs. \( r^3 \).

- **\( r = 1 \, \text{AU} = 1.496 \times 10^{11} \, \text{m} \)**:  
  - \( G M = 1.327 \times 10^{20} \, \text{m}^3 \text{s}^{-2} \),  
  - \( r^3 = (1.496 \times 10^{11})^3 = 3.347 \times 10^{33} \, \text{m}^3 \),  
  - \( T = 2\pi \sqrt{\frac{3.347 \times 10^{33}}{1.327 \times 10^{20}}} \approx 2\pi \sqrt{2.523 \times 10^{13}} \approx 3.156 \times 10^7 \, \text{s} \) (about 1 year),  
  - \( T^2 \approx 9.96 \times 10^{14} \, \text{s}^2 \),  
  - Check: \( \frac{4\pi^2}{G M} r^3 = (2.975 \times 10^{-19}) \times (3.347 \times 10^{33}) \approx 9.96 \times 10^{14} \). Matches!

- **\( r = 2 \, \text{AU} = 2.992 \times 10^{11} \, \text{m} \)**:  
  - \( r^3 = (2.992 \times 10^{11})^3 = 2.678 \times 10^{34} \, \text{m}^3 \),  
  - \( T = 2\pi \sqrt{\frac{2.678 \times 10^{34}}{1.327 \times 10^{20}}} \approx 2\pi \sqrt{2.019 \times 10^{14}} \approx 8.93 \times 10^7 \, \text{s} \) (about 2.83 years),  
  - \( T^2 \approx 7.97 \times 10^{15} \, \text{s}^2 \),  
  - Check: \( \frac{4\pi^2}{G M} r^3 = (2.975 \times 10^{-19}) \times (2.678 \times 10^{34}) \approx 7.97 \times 10^{15} \). Matches!

- **\( r = 3 \, \text{AU} = 4.488 \times 10^{11} \, \text{m} \)**:  
  - \( r^3 = (4.488 \times 10^{11})^3 = 9.041 \times 10^{34} \, \text{m}^3 \),  
  - \( T = 2\pi \sqrt{\frac{9.041 \times 10^{34}}{1.327 \times 10^{20}}} \approx 2\pi \sqrt{6.812 \times 10^{14}} \approx 1.64 \times 10^8 \, \text{s} \) (about 5.2 years),  
  - \( T^2 \approx 2.69 \times 10^{16} \, \text{s}^2 \),  
  - Check: \( \frac{4\pi^2}{G M} r^3 = (2.975 \times 10^{-19}) \times (9.041 \times 10^{34}) \approx 2.69 \times 10^{16} \). Matches!

#### Step 5: Conclusion
The model calculates \( T \) from \( r \) and \( M \), and when we square \( T \) and compare it to \( r^3 \), the relationship \( T^2 = \frac{4\pi^2}{G M} r^3 \) holds every time. The constant \( \frac{4\pi^2}{G M} \) stays the same for the Sun’s mass, proving the law works.

### Simple Solution
This model picks distances (like 1 AU, 2 AU, 3 AU), finds the speed and period using gravity, and checks that \( T^2 \) matches \( r^3 \) times a constant. For the Sun, 1 AU gives 1 year, 2 AU gives about 2.83 years, and 3 AU gives about 5.2 years—Kepler’s Third Law is spot on every time!
