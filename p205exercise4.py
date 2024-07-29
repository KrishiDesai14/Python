tuple=(11,22,33,44,55,66,77,88,99)
c=0

for x in tuple:
    if x % 2 == 0:
        print(x)
        c+=1

print("count=> ",c)
