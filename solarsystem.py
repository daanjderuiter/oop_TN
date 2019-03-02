from math import sqrt
import matplotlib.pyplot as plt
from scipy.constants import G, au
from vector import Vector

class Universe:

    def __init__(self, dt=60*60*24):
        """Initialises an empty universe with default time steps of a day"""
        self.planets = {}
        self.t = 0
        self.dt = dt

    def get_body(self, name):
        try:
            return self.planets[name]
        except KeyError:
            print(f'There is no planet with the name {name}!')

    def add_body(self, planet):
        name = planet.name
        if name in self.planets:
            raise NameError(f'A planet with the name {name} already exists!')
        else:
            self.planets[name] = planet

    def remove_body(self, name):
        try: 
            del self.planets[name]
        except KeyError:
            print(f'No planet with name {name} was present to begin with.')

    def forces(self):
        n = len(self.planets)
        forces = {}
        # Only running j from i halves the amount of required computations
        for planet in self.planets.values():
            total_force = Vector(0, 0, 0)

            for other_planet in self.planets.values():
                if planet is other_planet:
                    continue

                vector = planet.position - other_planet.position
                total_force += -G * planet.mass * other_planet.mass * \
                        vector / vector.norm()**3 

            forces[planet.name] = total_force

        return forces

    def update(self):
        for planet, force in self.forces().items():
            acceleration = force / self.planets[planet].mass

            self.planets[planet].velocity += acceleration * self.dt
            self.planets[planet].position += self.planets[planet].velocity * self.dt


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
earth = Planet('Earth', M_earth, (au, 0, 0), (0, sqrt(G*M_sun / au), 0))
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

