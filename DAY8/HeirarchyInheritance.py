class A:
    x,y=90,20
    def a1(self):
        print("This is from parent class x+y",self.x+self.y)
class B(A):
    a,b=100,200
    def b1(self):
        print("This is from child class a+b",self.a+self.b)
class C(A):
    c,d=70,80
    def c1(self):
        print("This is from child class c+d", self.c+self.d)
objb=B()
objb.b1()
objc=C()
objc.c1()