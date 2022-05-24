# Implements the Point class for representing points in the
# 2-D Cartesian coordinate system.

import math


class Point:
    # Create line object
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def __str__(self):
        return '(' + str(self.xCoord) + ',' + str(self.yCoord) + ')'

    def __eq__(self, other_point):
        return self.xCoord == other_point.xCoord and self.yCoord == other_point.yCoord

    # Return x coordinate of the point
    def get_x(self):
        return self.xCoord

    # Return y coordinate of the point
    def get_y(self):
        return self.yCoord

    # Shift point by x_inc and y_inc
    def shift(self, x_inc, y_inc):
        self.xCoord += x_inc
        self.yCoord += y_inc

    # Compute distance between two points
    def distance(self, other_point):
        rise = self.yCoord - other_point.yCoord
        run = self.xCoord - other_point.xCoord
        return math.sqrt(rise ** 2 + run ** 2)
