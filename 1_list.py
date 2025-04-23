list1=[i for i in range(0,50,1)]
list2=[i**2 for i in range(1,51,1)]
count=1
list3=[]
for i in range (97,123,1):
    str=""
    for j in range(0,count,1):
        str+=chr(i)
    count+=1
    list3.append(str)
print("LIST 1\n",list1)
print("LIST 2\n",list2)
print("LIST 3\n",list3)
