n=int(input("Enter limit=> "))
c=0
s=0

c1=0
s1=0

for i in range(1,n+1):

    if(i%2) == 0:
        print("Even")
        c1+=1
        s1+=i

    else:
        print("Odd")
        c+=1
        s+=i

print("Count of even=> ", c1, "Sum of even=> ", s1)
print("Count of odd=> ", c, "Sum of odd=> ", s)


