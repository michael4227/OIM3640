# 2.1
print((42*60+42)/1, 'seconds')

# 2.2
print(10/1.61, 'miles')


# 2.3 (time per mile in minutes and seconds)
# print(((42*60+42)/1) / (10/1.61)) #...second/mile
min = (((42*60+42)/1) / (10/1.61))//60
second = (((42*60+42)/1) / (10/1.61) - min*60)
print('time per mile is', min, "min", second, "seconds per mile")

# (miles/hour)
hour = (42*60+42)/3600  # number of hour
miles = (10/1.61)  # number of miles s
print('miles per hour is', miles/hour)
