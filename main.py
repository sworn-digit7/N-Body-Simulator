from body import Body
from simulation import Simulation
import matplotlib.pyplot as plt


sun = Body(
    name="Sun",
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

moon = Body(
    name="Moon",
    mass=7.342e22,
    position=(1.496e11 + 3.844e8, 0),
    velocity=(0, 29780 + 1022)
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


print(
    "What system would you like to simulate?\n"
    "1. Solar System\n"
    "2. Earth-Moon\n"
    "3. Custom\n"
)

choice = int(input("Enter choice: "))

years = int(
    input(
        "How many years would you like to simulate?\n\n"
        "Enter years: "
    )
)

timestep = int(input("Enter timestep in seconds: "))


if choice == 1:

    bodies = [
        sun,
        mercury,
        venus,
        earth,
        mars,
        jupiter,
        saturn,
        uranus,
        neptune
    ]


elif choice == 2:

    bodies = [
        earth,
        moon
    ]


elif choice == 3:

    bodies = []

    number_of_bodies = int(
        input("\nHow many bodies would you like to add? ")
    )

    for i in range(number_of_bodies):

        print(f"\n--- Body {i + 1} ---")

        name = input("Name: ")

        mass = float(
            input("Mass (kg): ")
        )

        x_position = float(
            input("X position (m): ")
        )

        y_position = float(
            input("Y position (m): ")
        )

        x_velocity = float(
            input("X velocity (m/s): ")
        )

        y_velocity = float(
            input("Y velocity (m/s): ")
        )

        body = Body(
            name=name,
            mass=mass,
            position=(x_position, y_position),
            velocity=(x_velocity, y_velocity)
        )

        bodies.append(body)


else:

    print("Invalid choice.")
    exit()



simulation = Simulation(
    bodies=bodies,
    timestep=timestep
)


initial_energy = simulation.calculate_total_energy()

total_seconds = years * 365.25 * 24 * 60 * 60

steps = int(total_seconds / timestep)

positions = simulation.run(steps)



for i in range(len(bodies)):

    x = [
        position[i][0]
        for position in positions
    ]

    y = [
        position[i][1]
        for position in positions
    ]

    plt.plot(
        x,
        y,
        label=bodies[i].name
    )


plt.title("N-Body Simulation")

plt.xlabel("x position (m)")

plt.ylabel("y position (m)")

plt.legend()

plt.grid()

plt.show()



final_energy = simulation.calculate_total_energy()

percentage_error = (
    abs(final_energy - initial_energy)
    / abs(initial_energy)
    * 100
)

print(
    f"The percentage error is {percentage_error}%"
)