# Getter (@property)          → allows reading the value like an attribute (p.age) instead of a method (p.get_age()).
# Setter (@property_name.setter) → Allows to put condition once 

class Student:
    def __init__(self,name,physics,chemistry,math):
        self.name=name
        self.physics =physics
        self.chemistry=chemistry
        self.math = math

    @property
    def calculate_average(self):
        # average= (self.physics+self.chemistry+self.math)/3
        # print(f'Physics,Chemistry and Math average is {average:.2f}')
        return (self.physics + self.chemistry + self.math) / 3

    @calculate_average.setter
    def calculate_average(self, new_average):
       self.math = new_average * 3 - (self.physics + self.chemistry)      # Example: adjust math to match new average

    # Usage
stu = Student("Shweta", 90, 90, 90)
print(stu.calculate_average)  # 90.0

# stu.calculate_average = 80
# print(stu.calculate_average)  # 80.0
# print(stu.physics, stu.chemistry, stu.math)  # 90, 90, 60