class Employee:
    def EMP(self,eID,eName,eSal):
        self.eID=eID
        self.eName=eName
        self.eSal=eSal
    def display(self):
        print(self.eID,self.eSal,self.eName)
class Student:
    def STU(self,sID,sName,sGrade):
        self.sID=sID
        self.sName=sName
        self.sGrade=sGrade
    def show(self):
        print(self.sID,self.sName,self.sGrade)
emp=Employee()
stu=Student()
emp.EMP(40,'Shweta',6000)
emp.display()
stu.STU(202,'John','B')
stu.show()
