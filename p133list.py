import random
n=int(input("Enter limit=>"))
list1=[]

for i in range(1,n+1):
    y=random.randint(-10,10)
    list1.append(y)


print(list1)
