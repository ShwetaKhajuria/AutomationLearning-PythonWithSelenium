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
        return (self.physics+self.chemistry+self.math)/3

stu=Student("Shweta",89,90,98)
print(stu.calculate_average)
stu.math=90
print(stu.calculate_average)



