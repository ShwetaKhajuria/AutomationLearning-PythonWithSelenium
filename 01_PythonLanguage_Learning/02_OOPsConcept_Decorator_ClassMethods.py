# Class Methods are:-
                # A class method is a method that belongs to the class, not the instance.
                # It takes cls (the class itself) as its first parameter instead of self.
                # Defined using the @classmethod decorator.


class Company:
    companyname="Google"
    city="Waterloo"
    Emp="11115"

    @classmethod
    def display(self):
        print(f"Your company name is {self.companyname},{self.city}"
              f"and you employee ID is {self.Emp}")


Company.display()
