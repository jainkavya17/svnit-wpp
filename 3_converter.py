class converter:
    def __init__(self,val,unit):
        f=1
        if unit == 'inches':
            f=2.54 
        elif unit == 'feet':
            f=30.48
        elif unit == 'yards':
            f=91.44
        elif unit == 'miles':
            f=160934
        elif unit == 'kilometers':
            f=100000
        elif unit == 'millimeters':
            f=0.1
        elif unit == 'meters':
            f=100
        else:
            f=1
        self.val=val*f
    def inches(self):
        return (self.val/2.54)
    def feet(self):
        return (self.val/30.48)
    def yards(self):
        return (self.val/91.44)
    def miles(self):
        return (self.val/160934)
    def kilometers(self):
        return (self.val/100000)
    def millimeters(self):
        return (self.val*10)
    def meters(self):
        return(self.val/100)
    def centimeters(self):
        return(self.val)
v=float(input("Enter value : "))
u=input("Enter unit : ")
c=converter(v,u)
while True :
    print("\nFOR CONVERSION TO:")
    print("Inches press 1")
    print("Yards press 2")
    print("Miles press 3")
    print("Millimeters press 4")
    print("Centimeters press 5")
    print("Meters press 6")
    print("Kilometers press 7")
    print("Exit press 8\n")
    n=int(input())
    if(n==8):
        break
    if n==1:
        print(c.inches(),"inches")
    elif n==2:
        print(c.yards(),"yards")
    elif n==3:
        print(c.miles(),"miles")
    elif n==4:
        print(c.millimeters(),"millimeters")
    elif n==5:
        print(c.centimeters(),"centimeters")
    elif(n==6):
        print(c.meters(),"meters")
    elif(n==7):
        print(c.kilometers(),"kilometers")
print("Out of system")

    
    