s=input("Enter a sentence : ")
s=s.lower()
s=s.replace(" ","") 
a=list(set(list(s))) 
a.sort()
b=[chr(i) for i in range(97,123)]
if b!=a:
    print("Not pangram")
else :
    print("Pangram")