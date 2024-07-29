while True:
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '@' for exit")
    option = input("Enter option=> ")

    if (option == '+'):
        n1=float(input("Enter number one=> "))
        n2=float(input("Enter number two=> "))
        print("Addition=> ", n1+n2)
    elif (option == '-'):
        n1=float(input("Enter number one=> "))
        n2=float(input("Enter number two=> "))
        print("Subtraction=> ", n1-n2)
    elif (option == '*'):
        n1=float(input("Enter number one=> "))
        n2=float(input("Enter number two=> "))
        print("Multiplication=> ", n1*n2)
    elif (option == '/'):
        n1=float(input("Enter number one=> "))
        n2=float(input("Enter number two=> "))
        print("Division=> ", n1/n2)
    elif (option == '@'):
        break
    else:
        print("Please enter valid option")
