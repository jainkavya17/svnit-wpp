import math
t=int(input())
num=[]
sum=0
for i in range(t):
    s=input()
    s+=" "
    n=0
    for x in s:
        if(x.isdigit()):
            n=(n*10)+int(x)
        else:
            num.append(n)
            n=0
for i in range(0,t*2,2):
    sum=0
    for x in range(num[i],num[i+1]+1):
        if math.sqrt(x).is_integer():
            sum+=1
    print(sum)
