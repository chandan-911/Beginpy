import time
timestamp =time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
# timestamp=int(time.strftime('%M'))
# print(timestamp)
# timestamp=int(time.strftime('%S'))
# print(timestamp)
if(hour>=0 and hour<12):
    print("Good Morning sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon sir")
elif(hour>=17 and hour<19):
    print("Good Afternoon sir")
else:
    print("Good Night sir")