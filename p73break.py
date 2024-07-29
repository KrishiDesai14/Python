while True:
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 to stop")

    choice=float(input("Enter option=> "))

    if choice == 1:
        n1=float(input("Enter number=> "))
        n2=float(input("Enter number=> "))
        print("Addition=> ",n1+n2)
    elif choice == 2:
        n1=float(input("Enter number=> "))
        n2=float(input("Enter number=> "))
        print("Subtraction=> ",n1-n2)
    elif choice == 3:
        n1=float(input("Enter number=> "))
        n2=float(input("Enter number=> "))
        print("Multiplication=> ")
    elif choice == 4:
        n1=float(input("Enter number=> "))
        n2=float(input("Enter number=> "))
        print("Division=> ",n1/n2)
    elif choice == 5:
        break
    else:
        print("Please enter valid option")


