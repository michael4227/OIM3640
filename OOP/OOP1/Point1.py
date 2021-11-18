class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
mich = Point()
mich.x = 3
mich.y = 4
print(mich)

def print_point(p):
    print(f'({p.x},{p.y})')

print_point(mich)