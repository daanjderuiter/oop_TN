from math import sqrt

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def norm(self):
        """Returns the norm of the vector"""
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __mul__(self, const):
        """Return a Vector scaled by a constant"""
        return Vector(self.x * const, \
                self.y * const, \
                self.z * const)

    def normalized(self):
        """Return the Vector, but normalized"""
        return self.scale(1/self.norm())

    def __matmul__(self, other):
        """Returns the dot product with another vector"""
        return self.x * other.x + \
                self.y * other.y + \
                self.z * other.z

    def cross(self, other):
        """Returns the cross product with another vector"""
        return Vector(self.y*other.z - self.z*other.y, \
                self.z*other.x - self.x*other.z, \
                self.x*other.y - self.y*other.x)


    def __add__(self, other):
        """Returns the sum with another vector"""
        return Vector(self.x + other.x, \
                self.y + other.y, \
                self.z + other.z)

    def __neg__(self):
        """Returns the additive inverse of the vector"""
        return Vector(-self.x, -self.y, -self.z)
    
    def __sub__(self, other):
        """Returns the difference with another vector"""
        return self + -other

    def __eq__(self, other):
        """Returns the equality with another vector"""
        return self.x == other.x and self.y == other.y and self.z == other.z

