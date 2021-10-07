prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter =='Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

name = 'zanjiesunmichael'
count = 0
for i in name:
    if i == 'a' or i =='e' or i =='i' or i =='o' or i =='u':
        count += 1
print(count)    


def count_letter(name, letter):
    count = 0
    for name in letter:
        count +=1
    return count
print(count_letter('michael', 'iae'))