# ex1
import abc


prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter =='Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

# ex2
word = 'New England Patriots'
count = 0
for letter in word:
        count = count + 1
print(count)

# ex3
# ex4
def any_lowercase1(s):
    '''the number of true stands for the number of lower cases in the s string'''
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):
    '''if there is a lower string c in string s, there is a true. the number of true stands for the number of of lower c'''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    '''the last character that is lower case in the string s'''
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    '''the index of the last lower case in the string'''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    '''if there are any upper cases in the string'''
    for c in s:
        if not c.islower():
            return False
    return True

#ex5

def rotate_word(s):
    for a in s:
        num = ord(a)+1
        a = chr(num)
    return s

rotate_word(abc)
