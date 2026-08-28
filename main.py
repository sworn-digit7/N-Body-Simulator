from body import Body
from simulation import Simulation
import matplotlib.pyplot as plt

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
