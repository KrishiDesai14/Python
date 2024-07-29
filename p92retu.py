def cube(n1):
    return n1*n1*n1
def max(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2

def add(n1,n2):
    return n1+n2

def calc(n1,n2):
    return n1+n2,n1-n2,n1*n2,n1/n2

n1=int(input("Enter number 1=> "))
n2=int(input("Enter number 2=> "))
c=cube(n1)
m=max(n1,n2)
a=add(n1,n2)

print("cube = ",c)
print("max = ",m)
print("add = ",a)
a,s,m,d=calc(n1,n2)
