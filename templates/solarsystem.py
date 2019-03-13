from math import sqrt
import matplotlib.pyplot as plt
from scipy.constants import G, au
from vector import Vector

class Universe:

    def __init__(self, dt=60*60*24):
        """Initialises an empty universe with default time steps of a day"""
        pass

    def add_body(self, planet):
        """Add a body to the universe"""
        pass

    def forces(self):
        """Computes the forces on all planets, and returns these forces
        as a collection of Vectors in a suitable format"""
        pass
    
    def update(self):
        """Updates positions and velocities to the next time point"""
        pass

class Planet:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = Vector(*position)
        self.velocity = Vector(*velocity)

    def __repr__(self):
        return f'Name: {self.name}\nMass: {self.mass} kg\nPosition: ' + \
                f'{tuple(self.position)}\nVelocity: {tuple(self.velocity)}'


# Demo
M_sun = 2e30
M_earth = 5.972e24
M_mars = 6.39e23

universe = Universe()
earth = Planet('Earth', M_earth, (au, 0, 0), (0, 29780, 0))
sun = Planet('Sun', M_sun, (0, 0, 0), (0, 0, 0))
mars = Planet('Mars', M_mars, (1.524*au, 0, 0), (0, 24131, 0))

universe.add_body(earth)
universe.add_body(sun)
universe.add_body(mars)

r_sun = []
r_earth = []
r_mars = []

for _ in range(700):
    r_sun.append(sun.position)
    r_earth.append(earth.position)
    r_mars.append(mars.position)

    universe.update()

plt.figure()
plt.plot([r.x for r in r_sun], [r.y for r in r_sun], 'o', label='Sun trajectory')
plt.plot([r.x for r in r_earth], [r.y for r in r_earth], label='Earth trajectory')
plt.plot([r.x for r in r_mars], [r.y for r in r_mars], label='Mars trajectory')
plt.legend()
plt.show()
