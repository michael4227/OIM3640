# 1
pi = 3.1415926
r = 5
volumn = (4/3)*pi*r**3
print(volumn)

# 2
cp = 24.95
dc = 1-0.4
unit = 60
sc = 3 + 0.75*(unit-1)
total_cost = cp*unit*dc - sc
print(total_cost)

# 3
# calculate time needed in seconds
time1 = 8*60+15
time2 = 3*(7*60+12)
time3 = time1
# calculate total time in minutes
tot_time = (time1+time2+time3)/60
print(tot_time)
print('the time arrived home is', 6+1, ':', (tot_time+52)-60, 'am')

# 4
print('{:.1f}'.format((89-82)/82*100), '%')