f1=open("abc","r")
f2=open("pqr", "w")
t=0

vowels=['a','e','i','o','u','A','E','I','O','U']

while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch in vowels:
        print(ch,end="")
        t=t+1
    f2.write(ch)

print("Total=> ", t)

f1.close()
f2.close()
