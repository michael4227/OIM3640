import random
num = random.randint(1,20)
i = 1
while i < 7:
    numinput = int(input(f' You have {7-i} chances, attempt{i}, guess between 1-20:-->'))
    if numinput < num:
        print('go bigger')
    elif numinput > num:
        print('go smaller')
    else:
        print(f'YOU ARE RIGHT, at attempt {i}')
        break
    i += 1
if i == 7:
    print('you failed after trying 6 times')
else:
    print('GAME OVER')