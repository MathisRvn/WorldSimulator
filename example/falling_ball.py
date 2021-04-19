import matplotlib.pyplot as plt
import WorldSimulator

world = WorldSimulator.World()

ball_mass = 1 # kg

class EarthAttraction(WorldSimulator.Vec3D):
    def __init__ (self):
        super().__init__()

    def compute(self, object, world): # this funxtion is call at every tick to compute the value of the force

        self.x = 0
        self.y = object.mass * -9.81
        self.z = 0

ball = WorldSimulator.Object(
    world,
    ball_mass,
    y = 1000 # 1000m of altitude
)
ball.forces.append(EarthAttraction())

time = []
ball_x = []
ball_y = []
ball_speed = []

for i in range(0, 1000):
    world.tick(1) # 1s = we compute the position every 60s
    ball_x.append(ball.x)
    ball_y.append(ball.y)
    time.append(i)
    ball_speed.append(ball.speed.y)
    if ball.y <= 0:
        ball.y = 0
        break


plt.scatter(ball_x, ball_y)
plt.show() # Snapshot of the position

plt.scatter(time, ball_speed)
plt.show() # The speed in function of time
