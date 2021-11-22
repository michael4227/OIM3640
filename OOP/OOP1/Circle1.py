from Point1 import *
import copy
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 50.0
box.corner.y = 50.0
p = copy.copy(box.corner)

class Circle:
    """Represents a circle.

    Attributes: center, radius
    """
circle1 = Circle()
circle1.center = Point()
circle1.center.x = 20
circle1.center.y = 40
circle1.radius = 75

# print(circle1.radius)


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
# 左下
    p = copy.deepcopy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

# 右下
    p.x += rect.width
    print_point(p.x)
    if not point_in_circle(p, circle):
        return False

# 右上
    p.y += rect.height
    print_point(p.y)
    if not point_in_circle(p, circle):
        return False

# 左上
    p.x -= rect.width
    print_point(p.x)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
# 左下
    p = copy.deepcopy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

# 右下
    p.x += rect.width
    print_point(p.x)
    if  point_in_circle(p, circle):
        return True

# 右上
    p.y += rect.height
    print_point(p.y)
    if  point_in_circle(p, circle):
        return True

# 左上
    p.x -= rect.width
    print_point(p.x)
    if  point_in_circle(p, circle):
        return True

    return False

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
