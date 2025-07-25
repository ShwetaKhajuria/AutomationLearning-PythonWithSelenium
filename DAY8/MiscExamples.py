''' How to override Methods
    Need to create one class-A
    Create one Method M1 to print
    Create child class B of A
    Create one method with same name M1
    create one class of object of class B
    "write a code to invoke M1 method from Class A with object of B"'''

class A:
    def M1(self):
        print("This is a M1 method of class A")
class B(A):
    def M1(self):
        print("This is a M1 method of Class B") #Overriding method
        super().M1()

ObjB=B()
ObjB.M1()


''' Need to create one class-X
    create two variables with values
    Create child class Y of X
    create two diff variables with values
    Create one method with name M3
    Method is having another two variables 
    "write a code to add all theses variables"'''

class X:
    a,b=20,30
class Y(X):
    x,y=40,50
    def M(self,r,s):
        print("r+s(Local variables)-",r+s)
        print("x+y(Class Variables)-",self.x+self.y)
        print("a+b (Class Variables as well)",self.a+self.b)
Objy=Y()
Objy.M(20,3)

'''How to override variables'''
class Parent:
    name="shweta"
class Child(Parent):
    name="Kunsh" #Ovverriding the variable value
    def Parentvar(self):
        print(super().name)

ObjChild=Child()
print(ObjChild.name)
ObjChild.Parentvar()

'''Overriding Methods'''
class Bank:
    def rateofinterest(self):
        return 0
class TD(Bank):
    def rateofinterest(self):
        return 10
class RBC(Bank):
    def rateofinterest(self):
        return 20
objTD=TD()
print(objTD.rateofinterest())
objRBC=RBC()
print(objRBC.rateofinterest())