from src.Vec3D import *
from src.Object import *

class World:

    def __init__ (self):
        self.objects = []
        self.time_speed = 1

    def tick (self, delta_time):
        for object in self.objects:
            object.applyForces(delta_time * self.time_speed)
        for object in self.objects:
            object.applySpeed(delta_time * self.time_speed)
