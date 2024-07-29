f1=open("abc","r")
f2=open("pqr","w")
f3=open("wxy","w")

vowels=['a','e','i','o','u','A','E','I','O','U']

while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch in vowels:
        f2.write(ch)
    else:
        f3.write(ch)
f1.close()
f2.close()
f3.close()

