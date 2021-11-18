from Point1 import *


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """
circle = Circle(r)
circle.center = Point()
circle.radius = r


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    if point.x < point.circle.center.x + circle.radius and point.y < point.circle.center.y + circle.radius:
        print('The point is in the circle')
    else:
        print('The point is not in the circle')

def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """


def main():
    box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 50.0
    # box.corner.y = 50.0

    # print(box.corner.x)
    # print(box.corner.y)

    # circle = Circle
    # circle.center = Point()
    # circle.center.x = 150.0
    # circle.center.y = 100.0
    # circle.radius = 75.0

    # print(circle.center.x)
    # print(circle.center.y)
    # print(circle.radius)

    # print(point_in_circle(box.corner, circle))
    # print(rect_in_circle(box, circle))
    # print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
