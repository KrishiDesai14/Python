import random
x=random.randint(1,30)
y=0
c=0
s=1
en=30
while x!=y:
    print("Range is ",s," and ",en)
    y=int(input("Enter value of y=> "))
    c = c+1
    if(y>x):
        print("please enter smaller number")
        en=y
    elif(y<x):
        print("Please enter greater number")
        s=y
    else:
        print("congratulations you guessed the right number")

print("you tried => ",c, "times")
