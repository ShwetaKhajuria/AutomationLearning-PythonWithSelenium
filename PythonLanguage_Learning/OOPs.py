# ******* How to create a class **********************
class MyClass:
    def MyFun(self): #Instance method
        print("My Function 1")
    def MyFun2(self): #Instance method
        print("My Function 2")
    def MyFun3(self,name): #Instance method
        print("Hi" + " " +name)
    @staticmethod
    def MyFun4(age): #Static method
        print(age)

# ****** How to call/use a class *****************
mc1=MyClass()
mc1.MyFun()
mc1.MyFun2()
mc1.MyFun3("Shweta")
#mc1.MyFun4(30)
MyClass.MyFun4(100)




