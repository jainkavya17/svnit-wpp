n1=int(input())
n2=int(input())
max=0
for i in range (n1,n2+1):
    for j in range(n1,n2+1):
        if(i^j>max):
            max=i^j
print(max)