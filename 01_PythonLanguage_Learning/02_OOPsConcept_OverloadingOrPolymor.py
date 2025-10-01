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

#Example-3 Overloading
class ComplexNumber:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(f'{self.real}i+{self.img}j')

    def __add__(self,num2):
        # newreal= self.real+num2.real
        # newimg=self.img+num2.img
        # return ComplexNumber(newreal,newimg)
        return ComplexNumber(self.real+num2.real,self.img+num2.img)

Num1=ComplexNumber(7,8)
Num1.shownumber()
Num2=ComplexNumber(3,4)
Num2.shownumber()
# Num3=Num1.complex_addition(Num2)
# Num3.shownumber()
Num3=Num1+Num2
Num3.shownumber()

# Example -4 Polymorphysm
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Polymorphism: same method name, different behavior
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())