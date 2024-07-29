n=int(input("Enter limit=> "))
c=0
s=0
for i in range (1,n+1):
    print(i,"  ", end="")
    c+=1
    s+=i

print("count=> ",c, "Sum=> ",s)
