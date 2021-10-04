import time
print(time.time())
ctime=time.time()
#ctime is in second
daynum = ctime/60/60/24
# how many whole days
print(ctime)
print(daynum)
lefthour = (ctime - daynum)
# professor, how can I use f-string to convert both ctime and daynum to number? 
print(f'{lefthour:.0f}')
#lefthours = ctime - seconds in number of days 
hournum = f'{(ctime-daynum*24):.1f}'
minnum = f'{(ctime-daynum*24*60*60-hournum*60*60):.1f}'
secnum = f'{(ctime-daynum*24*60*60-hournum*60*60-minnum*60):.1f}'
print(f'{daynum} days, {hournum} hours, {minnum} mins')

# // 整除， %余数， /除以
# answer：
import time
ctime=time.time()
daynum = ctime//60//60//24
type(daynum)
hournum = ctime//60//60%24
minnum = ctime//60%60
secondnum = ctime%60
print(f'{int(daynum)} days, {int(hournum)} hours, {int(minnum)} mins, and {int(secondnum)} seconds')

print(f'{daynum:d}')
