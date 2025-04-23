class bank:
    def __init__(self,name,accno):
        self.balance=0
        self.name=name
        self.accno=accno
    def deposit(self,val):
        self.balance+=val
        print("\nAmount deposited succesfully")
    def withdraw(self,val):
        if (val>self.balance):
            print("\nInsuficient balance")
            return
        else:
            print("\nWithdrawal sucessful")
            self.balance-=val
    def get(self):
        print("Current balance : ",self.balance)
name=input("Enter account holder name : ")
num=int(input("Enter account number : "))
cust=bank(name,num)
while(True):
    print("\nDeposit : 1")
    print("Withdraw : 2")
    print("Check balance : 3")
    print("Acc holder name ; 4")
    print("Acc number : 5")
    print("Exit : 6\n")
    n=int(input())
    if(n==1):
        d=float(input("Enter amount to be deposited : "))
        cust.deposit(d)
    elif(n==2):
        d=float(input("Enter amount for withdrawl : "))
        cust.withdraw(d)
    elif(n==3):
        cust.get()
    elif(n==4):
        print("\nName : ",cust.name)
    elif(n==5):
        print("\nAcc No. : ",cust.accno)
    elif(n==6):
        break
    else:
        print("\nWrong choice")