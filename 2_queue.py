class queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,val):
        self.q.append(val)
        print("Enqueued")
    def dequeue(self):
        if(self.isEmpty()):
            print("Underflow")
            return
        else:
            print("Popped : ",self.q[0])
            del self.q[0]
    def peek(self):
        print("Element at top : ",self.q[0])
    def isEmpty(self):
        if len(self.q)==0:
            return True
        return False
    def display(self):
        for x in self.q:
            print(x,end="<-")
        print("\n")
q=queue()
while(True):
    print("Enqueue : 1")
    print("Dequeue : 2")
    print("Peek : 3")
    print("Check if empty : 4")
    print("Display : 5")
    print("Exit : 6\n")
    n=int(input())
    if(n==1):
        num=int(input("Enter value to be enqueued : "))
        q.enqueue(num)
    elif(n==2):
        q.dequeue()
    elif(n==3):
        q.peek()
    elif(n==4):
        if q.isEmpty():
            print("Yes,empty")
        else:
            print("Not empty")
    elif(n==5):
        q.display()
    elif(n==6):
        break
    else:
        print("Wrong choice")
