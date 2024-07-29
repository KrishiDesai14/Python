from datetime import datetime

now = datetime.now()

time = now.strftime("%H:%M:%S")
print("time:", time)
