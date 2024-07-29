tuple=(11,23,4,23,5,7,14,21)
c=0
s=0

for x in tuple:
    if x % 7 == 0:
        print(x)
        c+=1
        s=s+x

print("count=> ",c, "sum=> ",s)
