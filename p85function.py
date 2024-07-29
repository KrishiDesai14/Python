
def add():
    print("For addition")
    x=int(input("Enter value of x=> "))
    y=int(input("Enter value of y=> "))
    print("Addition of",x," and ",y,"is=> ",x+y)


def max2():
    print("For Max between 2")
    x=int(input("Enter value of no1=> "))
    y=int(input("Enter value of no2=> "))
    if x>y:
        print("no1 is greater")
    else:
        print("no2 is greater")

def table():
    print("For table")
    n=int(input("Enter number=> "))
    for i in range(1, n+1):
        print(n,"X",i,"=",n*i)

def oddeven():
    print("Odd even")
    n=int(input("Enter number=> "))
    if n % 2 == 0:
        print("Its a even number")
    else:
        print("Its a odd number")

def positivenegative():
    print("Positive or negative")
    n=int(input("Enter number=> "))
    if n>0:
        print("Its a positive number")


def max3():
    print("Max between three")
    n1=int(input("Enter number 1=> "))
    n2=int(input("Enter number 2=> "))
    n3=int(input("Enter number 3=> "))

    if n1>n2 and n1>n3:
        print("Number one is bigger")
    elif n2>n1 and n2>n3:
        print("Number two is bigger")
    elif n3>n1 and n3>n2:
        print("Number three id bigger")
    else:
        print("Please enter valid number")

def areaofcircle():
    print("Area of circle")
    r=int(input("Enter value of radius=> "))

    print("Area of circle is=> ", 3.14*r*r)

def areaofrectangle():
    print("Area of rectangle")
    l=int(input("Enter length=> "))
    w=int(input("Enter width=> "))

    print("Area of rectangle=> ", l*w)



add()
max2()
table()
oddeven()
positivenegative()
max3()
areaofcircle()
areaofrectangle()
