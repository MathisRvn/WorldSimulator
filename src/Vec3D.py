import math

class Vec3D:

    def __init__ (self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2) # Pythagoran theorem


    def __add__(self, other):
        if issubclass(type(other), Vec3D):
            return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError('Excepting <class \'Vec3D\'> or a subclass but get '+str(type(other)))

    def __mul__(self, other):
        if (type(other) is int) or (type(other) is float):
            return Vec3D(self.x*other, self.y*other, self.z*other)
        else:
            raise TypeError('Excepting <class \'int\'> or <class \'float\'> but get '+str(type(other)))

    def __sub__(self, other):
        return self + (other * -1)

    def __eq__(self, other):
        return True if (self.x == other.x and self.y == other.y and self.z == other.z) else False

    def compute(self, obect=0, world=0):
        pass

    # function used to print the class
    def __repr__(self):
        return "Vec3D"+str((self.x, self.y, self.z))

    @staticmethod
    def generateColinearVector(vector_length, colinear_vector):
        k = vector_length / colinear_vector.length
        return colinear_vector * k
