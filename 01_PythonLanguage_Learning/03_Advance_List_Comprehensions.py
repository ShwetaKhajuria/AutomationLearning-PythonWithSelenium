# List Comprehension - is a compact way to create a new list
#            Formula - ["expression" for "a value" in "iterable" if "condition"]
from operator import ifloordiv

# Traditional way to write lists
double=[]
for x in range(1,11):
    double.append(x*2)
print(double)

# List comprehension
#double = ["expression" for "a value" in "iterable" if "condition"]
sdouble = [y*2 for y in range(1,11)]
print(sdouble)

#List Comprehension on strings
fruits = ["orange","apple","banana","strawberry"]
fruits =[fruit.upper() for fruit in fruits]
print("Uppercase fruits list =", fruits)
fruits =[fruit[0] for fruit in fruits]
print("1st letter ", fruits)


#List comprehension with if condition
num_list=[1,2,-4,6,-7,-8,9,-1,12]
print("Positive numbers in the list ", [num for num in num_list if num>=0])
print("Negative numbers in the list ", [num for num in num_list if num<0])
print("Even numbers in the list ", [num for num in num_list if num%2==0])
print("Odd  numbers in the list ", [num for num in num_list if num%2!=0])

# Find a grade that are passing
grades = [90,80,35,40,20,30]
print("Passing garde are-",[grade for grade in grades if grade>=35])