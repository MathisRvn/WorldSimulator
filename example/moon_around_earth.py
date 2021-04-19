import matplotlib.pyplot as plt
import WorldSimulator

world = WorldSimulator.World()

earth_mass = 6.9722 * 10**24 #kg
moon_mass = 0.07346 * 10**24 #kg
moon_to_earth_mean_distance = 384400 * 1000 #m

earth = WorldSimulator.Object(
    world,
    earth_mass,
)
earth.forces.append(WorldSimulator.GravitationnalForce())

moon = WorldSimulator.Object(
    world,
    moon_mass,
    x = moon_to_earth_mean_distance,
    speed=WorldSimulator.Vec3D(0, 1022, 0)
)
moon.forces.append(WorldSimulator.GravitationnalForce())

moon_x = []
moon_y = []
earth_x = []
earth_y = []

for i in range(0, 10000):
    world.tick(60) # 60s = we compute the position every 60s
    moon_x.append(moon.x)
    moon_y.append(moon.y)
    earth_x.append(earth.x)
    earth_y.append(earth.y)

plt.scatter(moon_x, moon_y)
plt.scatter(earth_x, earth_y)
plt.show()
