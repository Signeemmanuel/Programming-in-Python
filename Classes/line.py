# Implements a LineSegment class constructed from Point objects.

from point import Point


class LineSegment:
    # Create point object
    def __init__(self, from_point, to_point):
        self._point1 = from_point
        self._point2 = to_point

    def __str__(self):
        return '[' + str(self._point1) + ',' + str(self._point2) + ']'

    # get starting point
    def get_from_point(self):
        return self._point1

    # get ending point
    def get_to_point(self):
        return self._point2

    # get the length of the line segment
    def length(self):
        return Point.distance(self._point1, self._point2)

    # check if line segment is vertical
    def is_vertical(self):
        return self._point1.get_x() == self._point2.get_x()

    # get slope of line segment
    def slope(self):
        if self.is_vertical():
            return None
        rise = self._point2.get_y() - self._point1.get_y()
        run = self._point2.get_x() - self._point1.get_x()
        return rise / run


point_a = Point(1, 5)
point_b = Point(3, 9)
line = LineSegment(point_a, point_b)
print(line.slope())
print(line.is_vertical())
print(line.length())
print(point_a)
print(line)
print(point_b == point_a)
