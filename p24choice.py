
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

choice=float(input("Enter choice=> " ))

if (choice == 1):
    n1=float(input("Enter number one=> "))
    n2=float(input("Enter number two=> "))
    print("Addition=> ", n1+n2)
elif (choice == 2):
    n1=float(input("Enter number one=> "))
    n2=float(input("Enter number two=> "))
    print("Subtraction=> ", n1-n2)
elif (choice == 3):
    n1=float(input("Enter number one=> "))
    n2=float(input("Enter number two=> "))
    print("Multiplication=> ", n1*n2)
elif (choice == 4):
    n1=float(input("Enter number one=> "))
    n2=float(input("Enter number two=> "))
    print("Division=> ", n1/n2)
else:
    print("Please enter valid option")




