n=int(input("Enter limit=> "))

for i in range(1, n+1):
    if (i % 2) == 0:
        print(i, "even")
    else:
        print(i, "odd")
