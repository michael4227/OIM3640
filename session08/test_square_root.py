
# EX3
import math
math.sqrt(2)

a = 1
x = 2
print(f'a, mysqrt(a), math.sqrt(a), diff \n')
for i in range(11):
    epsilon = 0.0000001
    while True:
        sqrt = math.sqrt(a)
        diff = abs(y - sqrt)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    print(f'{a}, {y}, {sqrt}, {diff}')
    a += 1
