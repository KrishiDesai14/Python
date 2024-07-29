n=int(input("Enter limit=> "))
c=0
s=0
for i in range(1,n+1):
    if(i%2) == 0:
        print(i," + ",end="")
        c+=1
        s+=i

print("\nCount of even = ",c," Sum = ",s)

"""
1 2 3 4 5
1+2+3+4+5
1X2X3X4X5
-1+4-9+16-25
1+4+27+16+125
"""
