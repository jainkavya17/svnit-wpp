class password_manager:
    def __init__(self):
        self._all=[]
    @property
    def password(self):
        if self._all == []:
            return "No password history"
        else:
            return self._all[len(self._all)-1]
    @password.setter
    def password(self,password):
        if password in self._all:
            print("Cannot change password to old password")
        else:
            self._all.append(password)
            print("Password changed successfully")
    def is_correct(self,password):
        if self._all==[]:
            return "No password history"
        if password==self._all[len(self._all)-1]:
            return True
        else :
            return False
c=1
user=password_manager()
while c!=4:
    c=int(input("Set password : 1\nGet password : 2\nCheck password : 3\nExit : 4\n"))
    if(c==1):
        s=input("Enter new password : ")
        user.password=s
    if(c==2):
        print(user.password)
    if(c==3):
        s=input("Enter password to be checked : ")
        b=user.is_correct(s)
        if(b==True):
            print("Correct password")
        elif(b==False):
            print("Wrong password")
        else:
            print(b)
        