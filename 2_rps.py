import random
class rps():
    user=0
    comp=0
    def __init__(self,rounds,current):
        self.rounds=rounds
        self.current=current
    def game(self,choice):
        s=['rock','paper','scissor']
        a=random.choice(s)
        print("Computer's choice : ",a)
        if(choice==1):
            if(a=='rock'):
                print("Draw")
            elif(a=='paper'):
                print("Computer won")
                self.current+=1
                rps.comp+=1
            else :
                print("You won")
                self.current+=1
                rps.user+=1
        elif(choice==2):
            if(a=='rock'):
                print("You won")
                self.current+=1
                rps.user+=1
            elif(a=='paper'):
                print("Draw")
            else:
                print("Computer won")
                self.current+=1
                rps.comp+=1
        else:
            if(a=='rock'):
                print("Computer won")
                self.current+=1
                rps.comp+=1
            elif(a=='paper'):
                print("You won")
                self.current+=1
                rps.user+=1
            else:
                print("Draw")
n=int(input("Enter number of rounds : "))
round=n
u=rps(n,1)
print("WELCOME TO THE GAME")
while u.current<=round:
    print("To start the round press : 1")
    print("To check the current round number press : 2")
    print("To check the current scores press : 3\n")
    n=int(input())
    if(n==1):
        print("To choose rock press : 1")
        print("To choose paper press : 2")
        print("To choose scissor press : 3\n")
        c=int(input())
        u.game(c)
    elif(n==2):
        print("Current round : ",u.current)
    elif(n==3):
        print("Computer : ",rps.comp)
        print("You : ",rps.user)
if(rps.comp>rps.user):
    print("\nUh Oh!! Computer Won")
elif (rps.comp<rps.user):
    print("\nCongrats , you defeated computer!!")
else:
    print("\nGame ended in a draw")
    



