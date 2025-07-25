class R:
    x,y=10,20
    def m3(self):
        print("x and Y from class R", self.x,self.y)
class S(R):
    def M4(self):
        print("Addition of x and y",self.x+self.y)
class T(S):
    def M5(self):
        print("Substraction of x and y",self.x-self.y)
objt=T()
objt.M4()
objt.m3()
objt.M5()