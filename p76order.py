while True:
    print("Enter p for pizza(price=200)")
    print("Enter s for sandwitch(Price=180)")
    print("Enter n for pasta(price=150")
    print("Enter d for icecream(price=100)")
    print("Enter x for exit")
    choice=input("Enter choice=> ").lower()
    fbill=0

    if( choice == 'p'):
        n1=int(input("Enter Quantity of Pizza= "))
        print("Total= ",200*n1)
        fbill=fbill+200*n1
    elif( choice == 's'):
        n1=int(input("Enter Quantity of sandwitch= "))
        print("Total= ", 180*n1)
        fbill=fbill+180*n1
    elif( choice == 'n'):
        n1=int(input("Enter Quantity of pasta= "))
        print("Total= ",150*n1 )
        fbill=fbill+150*n1
    elif( choice == 'd'):
        n1=int(input("Enter Quantity of icecream= "))
        print("Total= ", 100*n1)
        fbill=fbill+100*n1
    elif( choice == 'x'):
        print("Final biil = ",fbill)
        break
    else:
        print("Please enter valid option")



