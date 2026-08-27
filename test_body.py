from body import Body
import pytest

# (name, mass, [position], [velocity])

def test_init():

    body = Body("Earth", 5.972e24, [1.496e11, 0], [0, 29_780])
    assert body.name == "Earth"
    assert body.mass == 5.972e24
    assert body.position == [1.496e11, 0]
    assert body.velocity == [0, 29_780]

   
def test_mass():
    body = Body("Earth", 5.972e24, [1.496e11, 0], [0, 29_780])

    with pytest.raises(ValueError):
        body.mass = -1

def test_coordinates():
    body = Body("Earth", 5.972e24, [1.496e11, 0], [0, 29_780])

    with pytest.raises(ValueError):
        body.position = 23
