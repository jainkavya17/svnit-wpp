t=int(input())
cycles=[]
for i in range(t):
    cycles.append(int(input()))
def height(n):
    temp=1.0
    for i in range (1,n+1):
        if(i%2==0):
            temp+=1
        else:
            temp*=2
    return temp
for x in cycles:
    print(height(x))