import random
d1={}
n=int(input("Enter limit=> "))

for i in range(1,n+1):
    rno=i
    marks=random.randint(1,30)
    d1[rno]=marks

print("No\tMarks")
print("*"*30)
c=0

for k,v in d1.items():
    if v>20:
        print(k,"\t",v,"pass")
        c+=1

print("Total number of pass=> ",c)
