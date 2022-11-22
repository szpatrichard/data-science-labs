"""Using Newton's gravitation formula write a Python program that asks an end user to enter
two values for mass of an object 1 and 2 and their distance r and then calculate F."""

from enum import Enum

class Constant(float, Enum):
    """Physical constants."""
    G = 9.8

class Object:
    """Object class."""
    def __init__(self, mass):
        try:
            if (isinstance(mass, int) or isinstance(mass, float)):
                if mass > 0:
                    self.mass = mass
        except ValueError as err:
            print(err)

    def calc_force(self, obj, r):
        """Calculates force of gravitational pull between two objects.

        Args:
            obj (Object): Second Object object.
            r (float): Distance between objects.

        Returns:
            float: Force of gravitational pull.
        """
        if not isinstance(obj, Object):
            return

        if not isinstance(r, int) and not isinstance(r, float):
            return

        try:
            F = Constant.G * (self.mass * obj.mass / pow(r, 2))
            return F
        except AttributeError as err:
            print(err)
            return

def masses_input(prompt):
    """Prompts for mass value.

    Args:
        prompt (str): A string to prompt the user.

    Raises:
        ValueError: _description_

    Returns:
        float: Mass of an object
    """
    m = float()
    while isinstance(m, float) and m <=0:
        try:
            m = float(input(prompt))
            if m <= 0:
                raise ValueError(f"invalid mass value: {m}")
            return m
        except ValueError as err:
            print(err)
            m = float()

def distance_input():
    """Prompts for distance value.

    Returns:
        float: Distance between two objects.
    """
    r = float()
    while isinstance(r, float):
        try:
            r = float(input("Distance between objects: "))
            return r
        except ValueError as err:
            print(err)
            
def add_distance():
    """Adds distance between to objects.

    Returns:
        list: List of edges.
    """
    edges_list = list()
    for x in range(2):
        m = masses_input(f"Mass of object {x + 1}: ")
        edge_obj = Object(m)
        edges_list.append(edge_obj)
    r = distance_input()
    edges_list.append(r)
    return edges_list

def print_force(force):
    """Prints results.

    Args:
        force (float): Force of gravitational pull.
    """
    print(f"F = {force}")

if __name__ == "__main__":
    objects = list()
    objects.append(add_distance())

    for obj in objects:
        obj1 = obj[0]
        obj2 = obj[1]
        distance = obj[2]

        force = obj1.calc_force(obj2, distance)
        print_force(force)
