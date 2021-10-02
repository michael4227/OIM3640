# pi = 3.1415926
# print(f'pi equals {pi:8.5f}.')

# s1 = 'a'
# s2 = 'ab'
# s3 = 'abc'
# s4 = 'abcd'

# print(f'{s1:>10}')
# print(f'{s2:>100}')
# print(f'{s3:>10}')
# print(f'{s4:8.10}, hi')

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter =='Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

# Write a function with loop that prints the following pattern.
# If n is 5, expected output is:

# a 
# b b 
# c c c 
# d d d d 
# e e e e e 
def loopprint(n):
    for i in range(n+1):
        print(str(i)*i)
loopprint(5)