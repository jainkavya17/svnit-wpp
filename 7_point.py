import math
class two_d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __sub__(self,other):
        d=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return d
    def dot(self,other):
        return((self.x*other.x)+(self.y*other.y))
    def cross(self,other):
        c=str((self.x*other.y)-(self.y*other.x))+" k "
        return c
class three_d(two_d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z
    def __sub__(self,other):
        d=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
        return d
    def dot(self,other):
        d=super().dot(other)+self.z*other.z
        return d
    def cross(self,other): 
        c=super().cross(other)
        c=str((self.y*other.z)-(self.z*other.y))+" i + "+str((self.z*other.x)-(self.x*other.z))+" j + "+c
        return c
print("Vector 1")
x1=int(input("Enter x co-ordinate : "))
y1=int(input("Enter y co-ordinate : "))
z1=int(input("Enter z co-ordinate : "))
print("Vector 2")
x2=int(input("Enter x co-ordinate : "))
y2=int(input("Enter y co-ordinate : "))
z2=int(input("Enter z co-ordinate : "))
if z1==0 and z2==0:
    v1=two_d(x1,y1)
    v2=two_d(x2,y2)
else:
    v1=three_d(x1,y1,z1)
    v2=three_d(x2,y2,z2)
print("Distance : ",v2-v1)
print("Dot product : ",v1.dot(v2))
print("Cross product : ",v1.cross(v2))