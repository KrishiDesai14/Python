while True:
    print("Enter 's' for square")
    print("Enter 'c' for cube")
    print("Enter 'e' for exit")
    choice=input("Enter choice=> ").lower()

    if( choice == 's'):
        n1=float(input("Enter number=> "))
        print("Square=> ",n1*n1)
    elif( choice == 'c'):
        n1=float(input("Enter number=> "))
        print("Cube=> ", n1*n1*n1)
    elif choice=='e':
        break
    else:
        print("Please enter valid option")
