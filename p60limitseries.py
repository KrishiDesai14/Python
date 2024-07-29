n=int(input("Enter limit=> "))
s=0

for i in range(1,n+1):
    print(i," + ",end="")
    s+=i

print("Sum=> ",s)
