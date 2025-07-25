#Example 1 - simple
class A:
    def M1(self):
        print("This is M1 method from Class A")
class B(A):
    def M2(self):
        print("This is M2 method from Class B")
b=B()
b.M2()
b.M1()


#Example 1 - with arg
class R:
    x,y=10,20
    def m3(self):
        print("x and Y from class R", self.x,self.y)
class S(R):
    def M4(self):
        print("Addition of x and y",self.x+self.y)
objs=S()
objs.M4()
objs.m3()
