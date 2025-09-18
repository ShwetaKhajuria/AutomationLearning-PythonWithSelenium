print("Example one :- ")
class MyClass():
    name='Shweta'
    def __init__(self,name):
        print("The value of Global Var = ",self.name)
        print("The value of local Var = ",name)
M=MyClass("Kunsh")

'''Ex I want to create Employee class,
          - in that I want to create one constructor which will accept three variables(ID, Name and Salary)
          - in that I want to create one more method which will print three Variables (ID, Name and Salary)'''
print("-----------------------------")
print("Example Two :- ")
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print("ID is:%d \nName is:%s \nSalary is:%d \n" %(self.id,self.name,self.salary))
    def bonus(self):
        bonus=self.salary/4
        print("Bonus is=",bonus)
Emp=Employee(1010,'John',14000)
Emp1=Employee(1011,'Sam',18000)
Emp.display()
Emp1.display()
Emp.bonus()



'''Ex I want to create Employee class,
          - in that I want to create one constructor which will accept three variables(ID, Name and Salary)
          - in that I want to create one more constructor which will print three Variables (ID, Name and Salary)'''
print("-----------------------------")
print("Example Three")
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def __str__(self):
        return(self.name)
Emp=Employee(1010,'John',14000)
print(Emp)



