n=int(input("Enter limit=> "))
c=0
m=1

for i in range (1,n+1):
    print(i," X ",end="")
    c+=1
    m*=i

print("Count=> ", c, "Multiplication=> ",m)
