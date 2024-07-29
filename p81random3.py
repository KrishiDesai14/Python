import random
c=0
c1=0

print("Enter 'a' for addition")
print("Enter 's' for suntraction")
print("Enter 'm' for multiplication")
print("Enter 'd' for division")
choice=input("Enter choice=> ")

if choice=='a':
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

elif choice =='s':
    for i in range(1,6):
        x = random.randint(1,50)
        y = random.randint(1,50)
        print("No1=> ", x)
        print("No2=> ",y)
        sub=int(input("Enter subratction of above "))
        if (x-y != sub):
            print("Its a wrong answer")
            c = c+1
        else:
            print("Right answer")
            c1 = c1+1

    print("wrong count=> ",c, "right count=> ", c1)

elif (choice == 'd'):
    for i in range(1,6):
        x = random.randint(1,50)
        y = random.randint(1,50)
        print("No1=> ", x)
        print("No2=> ",y)
        div=int(input("Enter division of above "))
        if (x/y != div):
            print("Its a wrong answer")
            c = c+1
        else:
            print("Right answer")
            c1 = c1+1

    print("wrong count=> ",c, "right count=> ", c1)

elif (choice == 'm'):
    for i in range(1,6):
        x = random.randint(1,50)
        y = random.randint(1,50)
        print("No1=> ", x)
        print("No2=> ",y)
        multi=int(input("Enter multiplication of above "))
        if (x*y != multi):
            print("Its a wrong answer")
            c = c+1
        else:
            print("Right answer")
            c1 = c1+1

    print("wrong count=> ",c, "right count=> ", c1)










