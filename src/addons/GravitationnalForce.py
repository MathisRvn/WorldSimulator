from src.Vec3D import *

class GravitationnalForce(Vec3D):
    def __init__ (self):
        super().__init__()

    def compute(self, object, world):
        gravitationnal_force = Vec3D()
        for obj in world.objects:
            if obj != object:
                # Newton's law of universal gravitation
                G = 6.674 * (10**-11)
                deplacement_vector = Vec3D(obj.x - object.x, obj.y - object.y, obj.z - object.z)
                if deplacement_vector.length != 0:
                    force_length = G * object.mass * obj.mass / deplacement_vector.length**2
                    force = Vec3D.generateColinearVector(force_length, deplacement_vector)
                    gravitationnal_force = gravitationnal_force + force

        self.x = gravitationnal_force.x
        self.y = gravitationnal_force.y
        self.z = gravitationnal_force.z
