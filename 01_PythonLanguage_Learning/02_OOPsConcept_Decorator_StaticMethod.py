# @staticmethod

# # Works like a normal function, but placed inside the class.
# # Does not take self or cls.
# Organizing related functions
# If you have utility/helper functions that are logically related to a class but don’t need to access its data, @staticmethod keeps them grouped together.
# Example: MathUtils.add() or DateUtils.is_leap_year()
#
# Cleaner Code
# Instead of having random global functions, you keep them under the class they belong to.
#
# No need for object creation
# You can call it directly with the class, without making an object.

# Real-life Example:
# Imagine you’re working with an Employee class. You might want a helper function to check if an employee ID is valid. That doesn’t depend on any specific employee, so it’s a static method:

class Employee:
    def __init__(self,emp_name,emp_ID,emp_Location):
        self.emp_name=emp_name
        self.emp_ID=emp_ID
        self.emp_Location=emp_Location

    def display_employee(self):
        print(f"Name={self.emp_name}"
              f"\nID={self.emp_ID}"
              f"\nLocation={self.emp_Location}")
    @staticmethod
    def validate_emp_ID(emp_ID):
       if len(str(emp_ID))>3:
           pass
       else:
           print("Please enter more than 3 digits")


Emp = Employee("Shweta","12",emp_Location="Waterloo")
Emp.display_employee()
Employee.validate_emp_ID(1982)
