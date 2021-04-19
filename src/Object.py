from src.Vec3D import *

class Object():

    def __init__(self, world, mass, x=0, y=0, z=0, speed=Vec3D(0, 0, 0)):
        self.world = world
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        entity = None
        self.forces = []
        self.world.objects.append(self)

    def applyForces(self, delta_time):

        force_total = Vec3D() # represent the sum of all forces which apply to the object
        for force in self.forces:
            force.compute(self, self.world)
            force_total = force_total + force

        # Newton law : force_sum = mass * speed variation / delta_time
        # speed variation = force_sum * (delta_time / mass)
        speed_variation = force_total * (delta_time / self.mass)
        self.speed = self.speed + speed_variation

    def applySpeed(self, delta_time):
        self.x += self.speed.x * delta_time
        self.y += self.speed.y * delta_time
        self.z += self.speed.z * delta_time
