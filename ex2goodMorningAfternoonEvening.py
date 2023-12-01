import time

hms = time.strftime('%H:%M:%S')
print(hms)

h = int(time.strftime('%H'))
if(h>6 and h<12):
    print("Good Morning")
elif(h>12 and h<18):
    print("Good Afternoon")
else:
    print("good Evening")