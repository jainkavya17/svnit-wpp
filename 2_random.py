import random
list=[]
for i in range(0,100,1):
    list.append(random.randint(0,1))
max=0
count=0
for i in list:
    if i==0:
        count+=1
    else:
        if(count>max):
            max=count
        count=0
print(list)
print("Longest run of 0 is ",max)
    