import time
h = int(time.strftime('%H'))

if h<12:
    print("Good morning")
elif h>12:
    print("Good evening")
else:
    print("Good night")






