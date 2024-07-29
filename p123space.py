f1=open("abc","r")
t=0

while True:
    ch=f1.read(1)
    if not ch:
        break

    if ch.isspace():
        t=t+1
    else:
        print(ch,end="")

f1.close()

print("\nNUmber of space=> ",t)
