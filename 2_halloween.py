t=int(input())
k=[]
for i in range(t):
    k.append(int(input()))
for x in k:
    h=x//2
    v=x-h
    print(h*v)
