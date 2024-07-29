list1=[11,55,90,33,44,22,11,44,55]
c=0
s=0
for x in list1:
    if x %11 == 0:
        print(x)
        c+=1
        s=s+x
        
print("Count = ",c," Sum = ",s)
