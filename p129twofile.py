f1=open("pqr","r")
f2=open("wxy","r")
f3=open("xyz","w")

while True:
    ch=f1.read(1)
    if not ch:
        break
    f3.write(ch)

while True:
    ch=f2.read(1)
    if not ch:
        break
    f3.write(ch)

f1.close()
f2.close()
f3.close()


