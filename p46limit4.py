n=int(input("Enter number=> "))
c=0
s=0

for i in range(1,n+1):
    print(i*i," + ",end="")
    c+=1
    s+=i

print("Count=> ", c, "Sum=> ",s)

