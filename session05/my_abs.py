# Ex3:
def my_abs(a):
    if a > 0:
        print(a)
    else:
        print(-a)
my_abs(-99)

# def my_abs2(a):
#     if a > 0:
#         return a
#     else:
#         return -a
# print (my_abs2(-99))

# Ex4:
def my_abs(a):
    if a > 0:
        print(a)
    else:
        print(-a)
    return a, -a
    print(my_abs(-123))

# Ex5: returning integer and floating numbers
a= input('Please enter a float or a integer:')
if isinstance(a, int() or float()) is True:
    def my_abs(a):
        if a > 0:
            print(a)
        else:
            print(-a)
        return a, -a
    print(my_abs(-123))
else:
    print('False')