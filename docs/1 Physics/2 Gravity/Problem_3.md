# Problem 3

 # # TASK1 

 Analyze the possible trajectories (e.g., parabolic, hyperbolic, elliptical) of a payload released near Earth.

# Elliptical Trajectory:

If the payload is released with a speed less than the "escape speed" (about 11.2 km/s near Earth) but enough to stay in orbit, it will follow an elliptical path. This means it loops around Earth in an oval shape, like a satellite.
Example: A payload dropped from a rocket in low Earth orbit with a gentle push might circle Earth in an ellipse.

# Parabolic Trajectory:

If the payload is released with exactly the escape speed (11.2 km/s), it follows a parabolic path. It moves away from Earth and just barely escapes gravity, slowing down as it goes but never returning.
Example: A payload given a precise kick to hit this speed would trace a curve that flattens out as it leaves Earth.

# Hyperbolic Trajectory:

If the payload is released with a speed greater than the escape speed, it follows a hyperbolic path. It escapes Earth’s gravity entirely and keeps going into space, moving faster than needed to break free.
Example: A payload launched with a strong boost (say, 15 km/s) would zip away from Earth in a wide, open curve.

# Simple Breakdown:

Speed < Escape Speed: Elliptical (loops around Earth).
Speed = Escape Speed: Parabolic (escapes but just barely).
Speed > Escape Speed: Hyperbolic (escapes easily).

# TASK2 

Perform a numerical analysis to compute the path of the payload based on given initial conditions (position, velocity, and altitude).

### Initial Conditions (Example):
- **Altitude**: 400 km above Earth’s surface (like a low Earth orbit).  
- **Position**: Starting at (x, y) = (6778 km, 0 km), where Earth’s radius is ~6378 km, so total distance from Earth’s center is 6778 km.  
- **Velocity**: 7.5 km/s horizontally (a bit below escape speed, close to orbital speed).  
- **Earth’s Gravity**: ~9.8 m/s² at the surface, but weaker at altitude (we’ll simplify it).

### Simple Numerical Approach:
We’ll track the payload’s path step-by-step over time, using small time steps (e.g., 1 second). Gravity pulls it toward Earth’s center, and its initial velocity keeps it moving. Here’s how it works:

1. **Gravity at Altitude**:  
   - Gravity decreases with distance from Earth’s center. At 6778 km, it’s roughly 8.7 m/s² (a simple approximation: 9.8 × (6378/6778)²).  
   - It pulls straight toward (0, 0), Earth’s center.

2. **Step-by-Step Path**:  
   - Start: Position = (6778 km, 0 km), Velocity = (0 km/s, 7.5 km/s) (horizontal).  
   - Each second:  
     - Update velocity: Gravity pulls downward (x-direction here), so x-velocity changes by -8.7 m/s² × 1 s = -0.0087 km/s.  
     - Update position: Move based on current velocity (e.g., x_new = x_old + vx × time).  

3. **Example Calculation (First Few Steps)**:  
   - **Time = 0 s**:  
     - Position: (6778, 0)  
     - Velocity: (0, 7.5)  
   - **Time = 1 s**:  
     - Gravity adjusts velocity: vx = 0 - 0.0087 = -0.0087 km/s, vy = 7.5 km/s.  
     - New position: x = 6778 - 0.0087 × 1 = 6777.9913 km, y = 0 + 7.5 × 1 = 7.5 km.  
   - **Time = 2 s**:  
     - Velocity: vx = -0.0087 - 0.0087 = -0.0174 km/s, vy = 7.5 km/s.  
     - Position: x = 6777.9913 - 0.0174 × 1 = 6777.9739 km, y = 7.5 + 7.5 = 15 km.  

4. **Trajectory Shape**:  
   - Over time, the payload curves downward while moving sideways. After many steps (e.g., 1000 seconds), it loops around Earth in an ellipse because the speed (7.5 km/s) is less than escape speed (11.2 km/s) but enough for orbit at this altitude.  
   - Distance from Earth’s center stays roughly constant (near 6778 km), confirming an elliptical path.

### Simple Result:
- With these conditions (400 km altitude, 7.5 km/s horizontal velocity), the payload follows an **elliptical trajectory**, orbiting Earth in an oval shape.  
- It doesn’t escape or crash right away—it circles Earth, gradually curving due to gravity.

#  # TASK3 

 Discuss how these trajectories relate to orbital insertion, reentry, or escape scenarios.




# Orbital Insertion:

What It Means: Getting the payload to stay in orbit around Earth, circling it over and over.
Trajectory Link: This happens with an elliptical path. If the payload is released at a good height (like 400 km) with enough sideways speed (like 7.5 km/s in our example), it loops around Earth without falling or flying off.
How It Works: The sideways speed keeps it from crashing down, and gravity keeps it from drifting away. Our example payload, moving at 7.5 km/s at 6778 km from Earth’s center, settles into an oval orbit—perfect for satellites or space stations.

#  Reentry: 

What It Means: The payload falls back to Earth, usually burning up or landing.
Trajectory Link: This ties to an elliptical path that gets too close to Earth. If the speed is too low (say, 5 km/s instead of 7.5 km/s) or it’s released lower down, gravity pulls it in faster than it can circle. The ellipse shrinks until it hits the atmosphere.
How It Works: In our example, if we slowed the payload or aimed it slightly downward, it’d curve back toward Earth instead of orbiting fully. Think of a capsule dropping from orbit—it follows a tight curve and lands.

# Escape:

What It Means: The payload leaves Earth completely, heading into space.
Trajectory Link: This matches a parabolic or hyperbolic path. At exactly 11.2 km/s (escape speed), it’s parabolic—just enough to break free. Faster than that (like 12 km/s), it’s hyperbolic, zooming off easily.
How It Works: If our payload got a big boost to 12 km/s instead of 7.5 km/s, it’d sail away from Earth, never looping back. This is how probes leave for the Moon or beyond.

# Simple Summary:

Elliptical: Stays in orbit (orbital insertion) or falls back if too slow/low (reentry).
Parabolic: Just escapes, barely breaking free (escape).
Hyperbolic: Flies off fast (escape).


#  # TASK4 

 Develop a computational tool to simulate and visualize the motion of the payload under Earth's gravity, accounting for initial velocities and directions.

 # step-by-step simulator that:

Tracks the payload’s position and velocity over time.
Shows how it moves under Earth’s gravity (pulling toward the center).
Lets you set the starting speed, direction, and height.
Visualizes the path (like a line curving around Earth).

# Set Up the Basics:

Earth is a point at (0, 0).
Payload starts at some distance (e.g., 6778 km, or 400 km above Earth’s 6378 km radius).
You pick the initial speed (e.g., 7.5 km/s) and direction (e.g., sideways, up, or angled).
Gravity pulls toward (0, 0), weaker the farther out (about 8.7 m/s² at 400 km).
Move It Step-by-Step:
Time ticks in small steps (like 1 second).

# Each step:

Gravity tugs the payload toward Earth a tiny bit (changes velocity).
Payload moves based on its current speed and direction.
Keep going for, say, 1000 steps to see the full path.

# Example Starting Point:

Position: (6778 km, 0 km) — 400 km up.
Velocity: 7.5 km/s sideways (so 0 km/s down, 7.5 km/s right).

# Each second:

Gravity pulls down a little (e.g., slows “down” speed by 0.0087 km/s).
Moves to a new spot (e.g., down a bit, right a lot).

# Visualize It:

Draw Earth as a circle (radius 6378 km).
Plot the payload’s position each step as a dot.
Connect the dots to see the path (e.g., an oval for orbit, a curve flying off for escape).