# Example -1
class Hello:
    def Sayhello(self,name=None):
        if name is not None:
            print("Hello ",name)
        else:
            print("Hello")
h=Hello()
h.Sayhello("Shweta")
h.Sayhello()

#Example-2
class addition:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
add=addition()
add.add()
add.add(10,20)
add.add(50,60,70)

