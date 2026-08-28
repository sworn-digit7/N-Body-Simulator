from body import Body
from simulation import Simulation
import matplotlib.pyplot as plt

sun = Body(
    name = "sun",
    mass=1.989e30,
    position=(0, 0),
    velocity=(0, 0)
)

mercury = Body(
    name="Mercury",
    mass=3.3011e23,
    position=(5.79e10, 0),
    velocity=(0, 47870)
)

venus = Body(
    name="Venus",
    mass=4.8675e24,
    position=(1.082e11, 0),
    velocity=(0, 35020)
)

earth = Body(
    name="Earth",
    mass=5.972e24,
    position=(1.496e11, 0),
    velocity=(0, 29780)
)

mars = Body(
    name="Mars",
    mass=6.4171e23,
    position=(2.279e11, 0),
    velocity=(0, 24070)
)

jupiter = Body(
    name="Jupiter",
    mass=1.8982e27,
    position=(7.785e11, 0),
    velocity=(0, 13070)
)

saturn = Body(
    name="Saturn",
    mass=5.6834e26,
    position=(1.434e12, 0),
    velocity=(0, 9680)
)

uranus = Body(
    name="Uranus",
    mass=8.6810e25,
    position=(2.871e12, 0),
    velocity=(0, 6800)
)

neptune = Body(
    name="Neptune",
    mass=1.0241e26,
    position=(4.495e12, 0),
    velocity=(0, 5430)
)

simulation = Simulation(
    bodies=[sun, earth],
    timestep=3600
)

initial_energy = simulation.calculate_total_energy()

positions = simulation.run(8760)

earth_x = [position[1][0] for position in positions]
earth_y = [position[1][1] for position in positions]

sun_x = [position[0][0] for position in positions]
sun_y = [position[0][1] for position in positions]

# print(len(positions))
# print(positions[0])
# print(positions[-1])

# plt.plot(earth_x, earth_y, label="Earth")
# plt.plot(sun_x, sun_y, label="Sun")

# plt.title("Earth's Orbit Around the Sun")
# plt.xlabel("x position (m)")
# plt.ylabel("y position (m)")
# plt.legend()
# plt.grid()
# plt.show()

final_energy = simulation.calculate_total_energy()

percentage_error = abs(final_energy - initial_energy) / abs(initial_energy) * 100

print("The percentage error is" + percentage_error)
