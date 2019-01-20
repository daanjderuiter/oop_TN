import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

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
        name = planet.get_name()
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
        forces = np.zeros((n, n, 3))
        planets = list(self.planets.keys())

        planet_1 = planet_2 = None

        # Only running j from i halves the amount of required computations
        for i in range(n):
            planet_1 = self.planets[planets[i]]

            for j in range(i, n):
                planet_2 = self.planets[planets[j]]
                vector = planet_1.position - planet_2.position

                forces[i, j] = -G * planet_1.mass * planet_2.mass * \
                        vector / np.linalg.norm(vector)**3 
                forces[j, i] = forces[i, j]

        return dict(zip(planets, forces.sum(axis=0)))

    def update(self):
        for planet, force in self.forces().items():

            acceleration = force / self.planets[planet].mass

            self.planets[planet].velocity, self.planets[planet].position = \
                    acceleration * self.dt, self.planets[planet].velocity * self.dt


class Planet:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return f'Name: {self.name}\nMass: {self.mass} kg\nPosition: {tuple(self.position)}\nVelocity: {tuple(self.velocity)}'

