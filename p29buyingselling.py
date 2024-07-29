b=input("Enter buying price=> ")
s=input("Enter selling price=> ")

if b>s:
    print(" The user has made loss")
elif s>b:
    print(" The user has made profit")
else:
    print(" Please enter valid number")
