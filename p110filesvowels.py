f1=open("abc","r")
tot =0

vowels=['a','e','i','o','u','A','E','I','O','U']
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch in vowels:
        tot= tot + 1

print("Total vowels are=> ",tot)

f1.close()

