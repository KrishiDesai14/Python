f1=open("abc","r")
t=0

vowels=['a','e','i','o','u','A','E','I','O','U']

while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch not in vowels:
        print(ch,end="")
        t=t+1

f1.close()

print("Total=> ",t)
