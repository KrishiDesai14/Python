student={11:"ram",13:"rja",45:"manav",55:"mansi"}
print(student)

print("No\tName")
print("*"*20)
for k,v in student.items():
    if len(v)==3:
        print(k,"\t",v)
print("*"*20)
