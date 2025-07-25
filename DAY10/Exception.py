
# # Example 1
# print("This is a starting point of a program")
# print("This is a starting point of a program")
# print("This is a starting point of a program")
#
# try:
#     print(x)
# except:
#     print("Execption occured")
# print("This is a Ending point of a program")
# print("This is a Ending point of a program")
# print("This is a Ending point of a program")
# print("This is a Ending point of a program")

# ## Example 2
# print("This is a starting point of a program")
# print("Inprogress...")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception occured and handled")
# print("Program Completed..")

#Example 3 : Multiple except blocks -try,except else, finally
# try:
#     num1,num2=10,0
#     result=num1/num2
#     print("Result is - ",result)
# except ZeroDivisionError:
#     print("ZeroDivisionError occured !!!!!")
# except SyntaxError:
#     print("syntax error!!!!!!")
# except:
#     print("Other type of Exception !!!!!!")
# else:
#     print("No Exception occured !!!!!!!!")
# finally:
#     print("This will occured everytime")

#Rising our own exception
def Enternum(num):
    if num<0:
        raise ValueError("Number is less than 0")
    elif num %2==0:
        print("even")
    else:
        print("odd")
num1=-1
try:
    Enternum(num1)
except ValueError:
    print("Value Error occured and handled")

