a=int(input("Enter age=> "))
g=input("Enter gender=> ")

if a>=18 and a<30:
    if g == 'm':
        print(" wage = 700")
    else:
        print(" Please enter valid number")

if a>=18 and a<30:
    if g == 'f':
        print(" wage = 750")
    else:
        print(" Please enter valid number")

if a>=30 and a<=40:
    if g == 'm':
        print("wage= 800")
    else:
        print("Please enter valid number")

if a>=30 and a<=40:
    if g == 'f':
        print("wage= 850")
    else:
        print("Please enter valid number")
