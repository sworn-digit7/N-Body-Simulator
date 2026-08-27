import math


class Simulation:
    def __init__(self, bodies, timestep):
        self.name = bodies
        self.timestep = timestep
        

# F = G m₁m₂ / r²

# body A position = (x₁, y₁)
# body B position = (x₂, y₂)

# dx = x₂ - x₁
# dy = y₂ - y₁

# r² = dx² + dy²

# r = √r²

# F = Gm₁m₂/r²


    def calculate_gravity(self, body, other_body):

        G = 6.67430 * 10 ** -11

        dx = other_body.position[0] - body.position[0]
        dy = other_body.position[1] - body.position[1]

        radius_squared = (dx ** 2) + (dy ** 2)

        F = (G * body.mass + other_body.mass) / radius_squared

        radius = math.sqrt(radius_squared)

        force_x = F * dx / radius
        force_y = F * dy / radius

        return force_x, force_y