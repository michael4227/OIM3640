# ex_1
def histogram(s):
    d = {}
    lst = list(s)
    for letter in lst:
        d[letter] = d.get(letter,0)+1
    return d
print(histogram('apple'))

def word_in_song(lyrics):
    d = {}
    lst_1 = lyrics.replace(',',' ').replace('.',' ')
    lst = lst_1.split()
    print(lst)
    for word in lst:
        d[word] = d.get(word,0)+1
    return d
print(word_in_song('apple pie, apple pear, pizza, pie, pie, pie'))

# ex_3
import os
print(os.getcwd())

# Assume words.txt is under data folder
f = open('data/words.txt')
line = f.readline()
d = {}
for line in f:
    d[line] = d.get(line,0)+1
# print(d.values())
def has_duplicates(d):
    for i in list(d.values()):
        if i == 1:
            continue
        else: 
            return True
    return False
has_duplicates(d)



