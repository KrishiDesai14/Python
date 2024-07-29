Flag = False
num=int(input("Enter number=> "))

if num == 1:
    print("Its not a prime number")
elif num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            Flag=True
            break

    if Flag:
        print("Its not a prime number")
    else:
        print("Its a prime number")


