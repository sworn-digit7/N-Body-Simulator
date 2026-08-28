import math


class Simulation:
    def __init__(self, bodies, timestep):
        self.bodies = bodies
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


#  f = m/a

    def calculate_acceleration(self, body, other_body):
        
        fx, fy = self.calculate_gravity(body, other_body)

        a_x = fx / body.mass
        a_y = fy / body.mass

        return a_x, a_y

    def calculate_total_acceleration(self, body):
        total_a_x = 0
        total_a_y = 0

        for other_body in self.bodies:

            if body != other_body:
                a, b = self.calculate_acceleration(body, other_body)
                total_a_x += a
                total_a_y += b


            return total_a_x, total_a_y

# vx_new = vx_old + ax × dt

# vy_new = vy_old + ay × dt

    def update_velocity(self, body):

        ax, ay = self.calculate_total_acceleration(body)

        new_vx = body.velocity[0] + ax * self.timestep
        new_vy = body.velocity[1] + ay * self.timestep

        return new_vx, new_vy

    def update_position(self, body):

        new_px = body.position[0] + body.velocity[0] * self.timestep
        new_py = body.position[1] + body.velocity[1] * self.timestep

        return new_px, new_py

    def step(self):
        ...