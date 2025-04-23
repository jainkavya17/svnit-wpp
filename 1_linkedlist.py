class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.size=0
    def insert(self,val,index):
        if self.head is None:
            self.size+=1
            self.head=Node(val)
            print("Inserted successfully")
            return
        c=1
        temp=self.head
        last=temp
        while (temp is  not None):
            if(c==index):
                break
            c+=1
            last=temp
            temp=temp.next
        newnode=Node(val)
        if(index==1):
            newnode.next=temp
            self.head=newnode
            print("Inserted successfully")
            self.size+=1
            return
        last.next=newnode
        newnode.next=temp
        print("Inserted successfully")
        self.size+=1
    def delete(self,index):
        if self.head is None:
            print("Already empty")
            return
        c=1
        temp=self.head
        last=temp
        f=0
        while (temp is  not None):
            if(c==index):
                f+=1
                break
            c+=1
            last=temp
            temp=temp.next
        if(f==1):
            print("\nDeleted : ",temp.data)
            if(index==1):
                self.head=temp.next
                self.size-=1
                del temp
                return
            last.next=temp.next
            self.size-=1
            del temp
        else:
            print("Wrong index choice")
    def display(self):
        c=1
        temp=self.head
        print("\n")
        while(temp is not None):
            print(c,"->",temp.data)
            c+=1
            temp=temp.next
ll=linkedlist()
print("Welcome to a new linked list")
while(True):
    print("\nInsert : 1")
    print("Delete : 2")
    print("Display : 3")
    print("Exit : 4\n")
    choice=int(input())
    if(choice==1):
        v=int(input("Enter value to be inserted : "))
        print("Enter the index ( 1 - ",(ll.size+1),")")
        i=int(input())
        ll.insert(v,i)
    elif(choice==2):
        print("Enter the index ( 1 - ",(ll.size),")")
        i=int(input())
        ll.delete(i)
    elif(choice==3):
        ll.display()
    elif(choice==4):
        break
    else:
        print("Wrong choice")
print("Out of the system")
    
        
        