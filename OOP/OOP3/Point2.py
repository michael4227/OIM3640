# from OOP1.Point1 import print_point


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        return (f'The point is at ({self.x},{self.y})')

# overwritting operators
    def __add__(self, another_point):
        new_x = self.x + another_point.x
        new_y = self.y +another_point.y
        return Point(new_x, new_y)

p1 = Point(3,4)
print(Point.print_point(p1))