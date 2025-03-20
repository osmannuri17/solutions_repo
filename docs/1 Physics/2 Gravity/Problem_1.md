# Problem 1
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