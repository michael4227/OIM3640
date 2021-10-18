
# EX3
import math
math.sqrt(2)

a = 1
x = 2
print(f'a    , mysqrt(a)                  , math.sqrt(a)          , diff \n')
for i in range(11):
    epsilon = 0.0000001
    while True:
        sqrt = math.sqrt(a)
        y = (x + a/x) / 2
        diff = abs(y - sqrt)
        if abs(y-x) < epsilon:
            break
        x = y
    print(f'{a:4}, {y:.20f}, {sqrt:<.20f}, {diff:<20.20f}')
    a += 1

import math


def mysqrt(a):
    """
    Use Newton’s method to compute square root of a positive number.

    Args:
        a(int): a positive number

    Returns:
        the square root of a.

    """
    epsilon = 1e-5
    x = 1
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x


def square_root(n):
    """
    Print the square root of integers from 1 to N-1

    Args:
        n(int): a positive number
    """
    # print("{:3} {:14} {:14} {:14}".format("a", "mysqrt(a)", "math.sqrt(a)", "diff"))
    print("a   mysqrt(a)      math.sqrt(a)   diff          ")
    print(f"{'-' * 3:3} {'-' * 13:14} {'-' * 13:14} {'-' * 17:17}")
    for a in range(1, n):
        print(
            f"{a:>3d} {mysqrt(a):<14.12g} {math.sqrt(a):<14.12g} {abs(mysqrt(a) - math.sqrt(a)):<14.12g}"
        )
square_root(10)

def main():
    # for i in range(1, 10):
    #     print('The square root of', i, 'is', mysqrt(i))
    square_root(11)


if __name__ == '__main__':
    main()