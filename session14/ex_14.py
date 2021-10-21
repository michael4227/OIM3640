# ex1
def sumall(*args):
    print(sum(args))

type(sumall(1,2,3))

# def printall(*args):
#     print(args)
# printall(1, 2.0, '3')

# ex2.1 (did not understand the question)
f = open('data/words.txt')
line = f.readline()
d1 = {}
d2 = {}
frequency = 0
for line in f:
    for letter in line:
        d2[letter] = d2.get(letter,0)+1
        frequency += d2.value()

# ex2.2
f = open('data/words.txt')
line = f.readline()
d = []
for line in f:
    d.append(line)
d1 = []
for i in d:
    size = len(i)
    i = i[:size-2]
    d1.append(i)
print(d1)
def anagram():
    for line in f:
        if list(line) == list(line).sort(reverse=True):
            print(line)
        else:
            continue
    print('finish checking for anagrams in d')
anagram(d1)