t=float(input("Enter tempreture=> "))

if (t<0):
    print("Freezing atmosphere")
elif (t<10):
    print("Very cold atmosphere")
elif (t<20):
    print("Cold atmosphere")
elif (t<30):
    print("Normal atmosphere")
elif (t<40):
    print("Hot atmosphere")
else:
    print("Please enter valid number")
