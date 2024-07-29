import random
d1={}
print("Enter 1 for pass")
print("Enter 2 for fail")
print("Enter 3 for both")
n=int(input("Enter option=> "))


for i in range(1,n+1):
    rno=i
    marks=random.randint(1,30)
    d1[rno]=marks

print("No\tMarks")
print("*"*30)

for k,v in d1.items():

    if n==1 and v>20:
        print(k,"\t",v,"pass")

    elif n==2 and v<20:
        print(k,"\t",v,"fail")

    elif n==3 and v>20:
        print(k,"\t",v,"pass")
    else:
        print(k,"\t",v,"fail")






