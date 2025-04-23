n=int(input("Enter the number : "))
def root(num):
    temp=num
    sum=0
    while temp>=10:
        while temp>0:
            d=temp%10
            sum+=d
            temp=temp//10
        temp=sum
        sum=0
    return temp
print("The digital root is : ",root(n))