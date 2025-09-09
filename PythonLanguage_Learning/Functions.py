# ***************** EXAMPLE 1 How to create a function *******************
def myfun():
    print("Hello World")

myfun()

# ***************** EXAMPLE 2 How to create a function *******************
def myfun1(name):
    print("Hello",name)

myfun1('shweta')

# ***************** EXAMPLE 3 How to create a function *******************
def cal(a,b):
    return(a+b)

print(cal(20,40))
sum=cal(200,400)
print(sum)

# ***************** EXAMPLE 4 How to create a function *******************
def myfun2():
    return

print(myfun2())

def myfun3():
    i=10

print(myfun3())

# ***************** EXAMPLE 5 How to create a function *******************
def myfunc4(x,y):
    return x+y

sum1=myfunc4(100,200)
print(sum1)

# ***************** Example 6 : How to create a function which returns a value **************
print("Example 6 : How to create a function which returns a value ")
class Employee:
    def bonus(self,sal):
        return(sal/4)
Emp=Employee()
bonus=Emp.bonus(2000)
print("Your bonus is - ",bonus)
