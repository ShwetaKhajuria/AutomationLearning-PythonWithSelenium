#without *agrs and **kwargs you can only add two digits
from mypy.message_registry import CANNOT_INFER_LAMBDA_TYPE
from mypy.types import names


def AdditionWithoutArgs(a,b):
    return a+b
print(AdditionWithoutArgs(6,7))


#*Args
def AdditionwithArgs(*args): #"args" text can be anything
    print(type(args)) # It will always be Tuple
    total =0
    for arg in args:
        total += arg
    return total
print(AdditionwithArgs(8,9,50,100))


#**Kwargs
def displayAddresswithkwargs(**kwargs):
    print(type(kwargs)) # It will always be dictionary
    for key,value in kwargs.items():
        print(f"{key}: {value}")

displayAddresswithkwargs(names="Shweta",street="1010 St W",Zipcode="N2L 212",City="Waterloo")

#*args and **kwargs together
def shippinglabels(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    print(kwargs.get("street"))
    print(kwargs.get("City"))
    print(kwargs.get("Zipcode"))

shippinglabels("Dr","Henry","Smith",street="1010 St W",Zipcode="N2L 212",City="Waterloo")


