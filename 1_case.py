import string
s=input("Enter a word ")
s2=""
c=1
for x in s:
    if c%2==0:
        x=str(x)
        s2+=x.swapcase()
        
    else:
        s2+=x
    c+=1
print(s2)