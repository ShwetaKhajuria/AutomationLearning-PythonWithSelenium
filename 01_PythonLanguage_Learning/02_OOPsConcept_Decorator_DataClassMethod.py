# @dataclass methods


# # @dataclass is a Python decorator from the dataclasses module (introduced in Python 3.7).
# # # It automatically generates boilerplate code (like __init__, __repr__, __eq__) for classes that mainly hold data.
# # # Less boilerplate → cleaner code.
# # # Easier debugging → auto__repr__ prints nice info.
# # # Data comparison → compare objects directly( ==).
from dataclasses import dataclass

@dataclass
class Student:
    name:str
    age:int
    grade:str

Stu1=Student("Shweta",23,"A")
Stu2=Student("Kunsh",11,"B")

print(Stu1)
print(Stu1==Stu2)
