class Bodies:
    def __init__(self, name, mass, x, y, vx, vy):
        self.name = name
        self.mass = mass
        self.position = x, y
        self.velocity = vx, vy



def main():
    variables()


def variables():
    for _ in range(0,2):
        name = input("Name of the body: ")
        mass = float(input("Mass of the body: "))
        position = float(input("The intial x and y position of the body: "))
        velocity = float(input("The initial x and y velocity of the body: "))
        return Bodies(name, mass, position, velocity)






main()
 
