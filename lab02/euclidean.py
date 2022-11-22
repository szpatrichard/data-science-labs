"""Write a program that takes two number as x and y coordinates of a point in a
Cartesian system and then calculate the Euclidean distance between the origin
of the Cartesian system and the point specified by x and y."""

import math

class Point:
    """Point on a 2D coordinate system."""
    def __init__(self, x, y):
        if isinstance(x, (float, int)):
            self.x = x
        if isinstance(y, (float, int)):
            self.y = y

    def get_x(self):
        """Get x coordinate.

        Returns:
            int: X coordinate
        """
        return self.x

    def get_y(self):
        """Get y coordinate.

        Returns:
            int: Y coordinate
        """
        return self.y

    def calc_distance(self, point):
        """Calculates distance between two points.

        Args:
            point (Point): Another point object.

        Returns:
            float: Distance between two points.
        """
        if not isinstance(point, Point):
            return
        d = math.sqrt((pow(point.x - self.x, 2) + pow(point.y - self.y, 2)))
        return d

if __name__ == "__main__":
    p1 = Point(5, 6)
    p2 = Point(3, 5)
    distance = p1.calc_distance(p2)
    print(distance)
