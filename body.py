class Body:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, m):
        if m < 0:
            raise ValueError("Mass can not be negative!")
        self._mass = m

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, p):
        if not isinstance(p, (list, tuple)) or len(p) != 2:
            raise ValueError("Position must be given in a coordinate with numbers")
        elif not isinstance(p[0], (float, int)) or not isinstance(p[1], (float, int)):
            raise ValueError("Position must be given in a coordinate with numbers")
        self._position = p

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, v):
        if not isinstance(v, (list, tuple)) or len(v) != 2:
            raise ValueError("Velocity must be given in a coordinate with numbers")
        if not isinstance(v[0], (float, int)) or not isinstance(v[1], (float, int)):
            raise ValueError("Velocity must be given in a coordinate with numbers")
        self._velocity = v




