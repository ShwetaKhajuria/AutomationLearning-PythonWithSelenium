# **** when the var name are different ***************

i,j=10,20 #Global variables
class MyCLass:
    a,b=30,40 #Class Variables
    def add(self,x,y): #Local Variables
        print("x and y are local variables",x+y)
        print("a and b are class variables",self.a+self.b)
        print("i and j are Global variables ",i+j)

MC=MyCLass()
MC.add(20,30)



# **** when the var name are SAME ***************
print("**** when the var name are SAME ***************")
l,m=20,30 #Global variables
class MyClass1:
    l,m=500,600 #Class variables
    def prnt(self,l,m): #Local variables
        print("l and m are local variables",l,m)  #local var
        print("l and m are class variables",self.l,self.m)
        print("l and m are Global variables ",globals()['l'],globals()['m'])
MC1=MyClass1()
MC1.prnt(3000,4000)


# ************ One class which has multiple objects ***********************
class MyClass2:
    def display(self,name):
        print("This is the name - ",name)

obj1=MyClass2()
obj1.display("Shweta")
obj1.display("Khajuria")

obj2=MyClass2()
obj2.display("Kunsh")

obj3=MyClass2()
obj3.display("Priyeadarshi")




