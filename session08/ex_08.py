#ex1.1
sum = 0
for i in range(11):
    print(f'before adding, sum is: {sum}')
    sum = i + sum
    print(f'after adding, sum is: {sum}')
print(sum)

#ex1.2
sum = 0
for i in range(1001):
    # print(f'before adding, sum is: {sum}')
    sum = i + sum
    # print(f'after adding, sum is: {sum}')
print(sum)

#ex1.3 odd
sum = 0
for i in range(1001):
    if i%2 == 1:
        print(f'before adding, sum is: {sum}')
        sum = i + sum
        print(f'after adding, sum is: {sum}')
    else:
        sum = sum
        print(f'not adding even number')
print(sum)
# or
sum = 0
for i in range(1,1000,2):
    sum += i
print(sum)

#ex1.3 even
sum = 0
for i in range(1001):
    if i%2 == 0:
        print(f'before adding, sum is: {sum}')
        sum = i + sum
        print(f'after adding, sum is: {sum}')
    else:
        sum = sum
        print(f'not adding even number')
print(sum)
# or
sum = 0
for i in range(2,1001,2):
    sum += i
print(sum)

#ex2.1 (1)
# on iteration 0, count = 1 
# on iteration 1, count = 2 
# on iteration 2, count = 3
# on iteration 3, count = 4
# on iteration 4, count = 5
#--------
# on iteration 0, count = 1 
# on iteration 1, count = 2 
# on iteration 2, count = 3
# on iteration 3, count = 4
# on iteration 4, count = 5
#ex2.1 (3)
# print will be execute 5 times
# the largest value for iteration is 4
# the largest value for count is 12, space and ; will all counted in the string
# the smallest value for count is 1, because the iteration will break if Iteration is an even number, when count is only added once.


iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

# re-ex1.1
iteration = 0
i = 0
while iteration < 10:
    i += 1 + iteration
    iteration += 1
print(i)

# re-ex1.2
iteration = 0
i = 0
while iteration < 1000:
    i += 1 + iteration
    iteration += 2
print(i)

# re-ex1.3
iteration = 0
i = 0
while iteration < 1000:
    i += 1 + iteration
    iteration += 2
print(i)

# EX3
while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y