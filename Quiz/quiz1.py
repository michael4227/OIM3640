"""
Question 1:

Given 2 integers, a and b, return True if one of them is 2021 or their sum is 2021 or their difference is 2021. Return False otherwise.

"""


def is_2021(a, b):
    """
    Given 2 integers, a and b, return True if one of them is 2021 or their sum is 2021 or their difference is 2021. Return False otherwise.
    """
    if a == 2021:
        return('true')
    elif b == 2021:
        return('true')
    elif a+b == 2021:
        return('true')
    elif abs(a-b) == 2021:
        return('true')
    else:
        return('false')

# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(is_2021(2021, 2))
# # expect: True
# print(is_2021(2, 2021))
# # expect: True
# print(is_2021(2000, 21))
# # expect: True
# print(is_2021(10, 2031))
# # expect: True
# print(is_2021(2020, 21))
# # expect: False

"""
-----------------------------------------------------------------------
Question 2:

Write a function with loop(s) that computes the average of square of all
integers between 1 and n (inclusive). 
For example: if n is 5, the average is (1*1+ 2*2+ ... + 5*5)/5 = 11.0 
"""


def calculate_avg(n):
    """
    Given integer n, return the average of cubes of all the integers between 1 and n (inclusive).
    """
    sum = 0
    for i in range(n+1):
        sum = sum + i*i
    sum  = sum/n
    return sum


# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(calculate_avg(1))
# # expect: 1.0
# print(calculate_avg(5))
# # expect: 11.0


"""
-----------------------------------------------------------------------
Question 3:

Write a function with loop that prints the following pattern.
If n is 5, expected output is:

a 
b b 
c c c 
d d d d 
e e e e e 

Hint: use ord() and chr()

If it is difficult for you, try to print the following pattern first:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def print_letters(n):
    """printing a to n in n lines"""
    for i in range(n+1):
        print(f'{chr(96+i)} '*i)
#     for i in range(n+1):

# When you've completed your function, uncomment the
# following lines and run this file to test!
print_letters(7)
# # expect:
# # a
# # b b
# # c c c
# # d d d d
# # e e e e e

# print_letters(9)
# # expect:
# # a
# # b b
# # c c c
# # d d d d
# # e e e e e
# # f f f f f f
# # g g g g g g g
# # h h h h h h h h
# # i i i i i i i i i


def func(n):
    return (n)
print(func('apple'))