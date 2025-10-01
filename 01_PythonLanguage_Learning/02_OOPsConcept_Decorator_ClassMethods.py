# Class Methods are:-
                # A class method is a method that belongs to the class, not the instance.
                # It takes cls (the class itself) as its first parameter instead of self.
                # Defined using the @classmethod decorator.


class Company:
    def __init__(self,companyname,city,Emp):
        self.companyname=companyname
        self.city=city
        self.Emp=Emp
    #@classmethod
    def display(self):
        print(f"Your company name is {self.companyname},{self.city} and you employee ID is {self.Emp}")


comp=Company("Google","Waterloo","21234")
#comp.display()
Company.display()
