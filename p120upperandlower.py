f1=open("abc", "r")
t1=0
t2=0

while True:
    ch=f1.read(1)

    if not ch:
        break
    if ch.isupper():
        t1=t1+1
    elif ch.islower():
        t2=t2+1

print("Total number of upper case letter=> ",t1)

print("Total number of lower case letter=> ",t2)



