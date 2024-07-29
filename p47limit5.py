n=int(input("Enter limit=> "))
c=0
s=0
c1=0
s1=0

for i in range(1, n+1):
    if(i%2) == 0:
        print(i*i," + ",end="")
        c+=1
        s+=i
    else:
        print(i*i," - ",end="")
        c1+=1
        s1+=i


print("Count of even=> ",c, "Sum of even=> ", s)
print("Count of odd=> ",c1, "Sum of odd=> ",s1)
