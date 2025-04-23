sample=[x for x in range(1,10001,1)]
classes={0:[],1:[],2:[],3:[],4:[]}
for x in sample:
    rem=x%5
    classes[rem].append(x)
u=set()
for i in range (0,5):
    u=u.union(set(classes[i]))
if list(u)==sample:
    print("Verified")
else:
    print("Not verified")