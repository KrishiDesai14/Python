n=int(input("Enter number=> "))
d=int(input("Divisiable by=> "))
c=0
s=0
c1=0
s1=0

for i in range(1, n+1):
    if i % 7 == 0:
        if i % 2 == 0:

        print(i,"Divisiable and even")
        c+=1
        s+=i
    else:
        print(i,"Divisiable and odd")
        c1+=1
        s1+=i


    print("Count=> ",c, "Sum=> ",s)


