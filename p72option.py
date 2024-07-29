while True:
    print("Enter 1 for square")
    print("Enter 2 for cube")
    print("Enter 3 for exit")
    choice=int(input("Enter choice=> "))
    if( choice == 1):
        n1=float(input("Enter number=> "))
        print("Square=> ",n1*n1)
    elif( choice == 2):
        n1=float(input("Enter number=> "))
        print("Cube=> ", n1*n1*n1)
    elif choice==3:
        break
    else:
        print("Please enter valid option")

