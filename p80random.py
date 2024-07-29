import random
c=0
c1=0
for i in range(1,6):
    x = random.randint(1,50)
    y = random.randint(1,50)
    print("No1=> ", x)
    print("No2=> ",y)
    add=int(input("Enter addition of above "))
    if (x+y != add):
        print("Its a wrong answer")
        c = c+1
    else:
        print("Right answer")
        c1 = c1+1

print("wrong count=> ",c, "right count=> ", c1)


