f1=open("abc","r")
f2=open("pqr","w")

while True:
    ch=f1.read(1)
    if not ch:
        break
    f2.write(ch)

f1.close()
f2.close()

print("Copied")

"""
1) 1 file to other , space X , pass
2) 1 file to other , vowels X
3) 1 file to 2 and 3 rd vowel , other
4) 1 file to 2 and 3 upper lower

"""
