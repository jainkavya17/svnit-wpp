t=int(input())
words=[]
for i in range(t):
    words.append(input())
for s in words:
    n=len(s)
    count=0
    if n%2==0:
        n=n//2
    else:
        n=(n//2)+1
    for i in range(n):
        c1=ord(s[i])
        c2=ord(s[0-(i+1)])
        if(c1==c2):
            continue
        elif(c1<c2):
            while(c1!=c2):
                c2-=1
                count+=1
        else:
            while(c1!=c2):
                c1-=1
                count+=1
    print(count)