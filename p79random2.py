import random
x = random.randint(1,50)
y= random.randint(1,50)

print("No1=> ", x)
print("No2=> ",y)

add=int(input("Enter addition of above "))
if (x+y != add):
    print("Its a wrong answer")
else:
    print("Right answer")
