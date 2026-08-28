from body import Body
from simulation import Simulation

sun = Body(
    name = "sun",
    mass=1.989e30,
    position=(0, 0),
    velocity=(0, 0)
)

earth = Body(
    name = "Earth",
    mass=5.972e24,
    position=(1.496e11, 0),
    velocity=(0, 29780)
)

simulation = Simulation(
    bodies=[sun, earth],
    timestep=3600
)

positions = simulation.run(8760)

# print(len(positions))
# print(positions[0])
# print(positions[-1])