import time
print(time.time())
ctime=time.time()
#ctime is in second
daynum = ctime/60/60/24
daynum = f'{daynum:.1f}'
# how many whole days
print(daynum)
lefthour = (ctime - daynum)
# professor, how can I use f-string to convert both ctime and daynum to number? 
print(lefthour)
#lefthours = ctime - seconds in number of days 
hournum = f'{(ctime-daynum*24):.1f}'
minnum = f'{(ctime-daynum*24*60*60-hournum*60*60)}'
secnum = f'{(ctime-daynum*24*60*60-hournum*60*60-minnum*60)}'
print(f'{daynum} days, {hournum} hours, {minnum} mins')

