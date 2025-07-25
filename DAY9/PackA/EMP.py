class Employee:
    def __init__(self,eName,eSal,eId):
        self.eName=eName
        self.eSal=eSal
        self.eId=eId
    def DisplayEMP(self):
            print("This is a method under Pack A/Employee class- ",self.eName,self.eSal,self.eId)
