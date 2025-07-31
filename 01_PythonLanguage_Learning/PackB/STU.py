class Student:
    def __init__(self,sName,sId,sGrade):
        self.sName=sName
        self.sId=sId
        self.sGrade=sGrade
    def DisplaySTU(self):
        print("This is a method under Pack B/Student class- Name- %s , ID- %d , Grade- %s" %(self.sName,self.sId,self.sGrade))

