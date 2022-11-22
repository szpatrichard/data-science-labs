"""Write a program that asks the user to enter radius of a circle and then calculate the area of the
circle using the following formula: area = 𝜋𝑟2 where 𝜋 = 3.14 and r is the radius, then print
the value of the area.
"""

import math

class Circle:
    """Circle class."""
    def __init__(self, r = float):
        try:
            if (isinstance(r, float) or isinstance(r, int)) and r > 0:
                self.radius = r
        except TypeError as err:
            print(err)

    def __str__(self):
        try:
            return f"Circle with radius {self.radius}"
        except AttributeError as err:
            print(err)
            return None

    def calc_area(self):
        """Calculates the area of the circle based on its radius.

        Returns:
            float: Area of circle.
        """
        try:
            return math.pi * pow(self.radius, 2)
        except AttributeError as err:
            print(err)
            return None

def radius_input():
    """Asks for a radius value of circle.

    Raises:
        ValueError: When invalid radius value is supplied.

    Returns:
        float: Radius of circle.
    """
    r = float()
    while isinstance(r, float) and r <= 0:
        try:
            r = float(input("Enter radius of circle: "))
            if r <= 0:
                raise ValueError(f"invalid radius value: {r}")
            return r
        except ValueError as err:
            print(err)
            r = float()

def print_area(circle):
    """Prints summary about a Circle object.

    Args:
        circle (Circle): Circle object.
    """
    print(c)
    area = circle.calc_area()
    print(f"Area: {area:.2f}")

if __name__ == "__main__":
    radius = radius_input()
    c = Circle(radius)
    print_area(c)
