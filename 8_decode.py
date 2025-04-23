def decodeMsg(str1):
    n=len(str1)
    l=[[] for _ in range(n+1)]
    l[0]=[""]
    for i in range(1,n+1):
        if str1[i-1]!='0':
            for s in l[i-1]:
                l[i].append(s+chr(int(str1[i-1])+64))
        if i>1 and "10"<= str1[i-2:i]<="26":
            for s in l[i-2]:
                l[i].append(s+chr(int(str1[i-2:i])+64))
    return l[n]

msg="11106"
print(decodeMsg(msg))