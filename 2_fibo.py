t=int(input())
num=[]
for i in range(t):
    num.append(int(input()))
def isfibo(n):
    a=0
    b=1
    c=0
    while c<n:
        c=a+b
        a=b
        b=c
    if(c==n):
        return True
    else:
        return False
for x in num:
    if(isfibo(x)):
        print("IsFibo")
    else:
        print("IsNotFibo")



