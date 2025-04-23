t=int(input())
words=[]
for i in range(t):
    words.append(input())
for x in words:
    n=len(x)-1
    s=list(x)
    index=-1
    while(n>0):
        if(s[n]>s[n-1]):
            s[n],s[n-1]=s[n-1],s[n]
            index=n
            break
        else:
            n-=1
    if(index!=-1):
        s1=''.join(s)
        s2=s1[:index]
        s3=''.join(sorted(s1[index:]))
        s2+=s3
        print(s2)
    else:
        print("No answer")
        