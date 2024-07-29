import time
presenttime = time.localtime()
tformat = time.strftime("%I:%M %p", presenttime)
print(tformat)
