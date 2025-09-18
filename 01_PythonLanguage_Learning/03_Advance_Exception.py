
# # Example 1
print("This is a starting point of a program")
print("This is a starting point of a program")
print("This is a starting point of a program")

try:
    print(x)
except:
    print("Execption occured")
print("This is a Ending point of a program")
print("This is a Ending point of a program")
print("This is a Ending point of a program")
print("This is a Ending point of a program")

# ## Example 2
print("This is a starting point of a program")
print("Inprogress...")
try:
    print(10/0)
except ZeroDivisionError:
    print("Exception occured and handled")
print("Program Completed..")

#Example 3 : Multiple except blocks -try,except else, finally
try:
    num1,num2=10,0
    result=num1/num2
    print("Result is - ",result)
except ZeroDivisionError:
    print("ZeroDivisionError occured !!!!!")        #only execute if the try box code fails with zerodivisionerror
except SyntaxError:
    print("syntax error!!!!!!")                     #only execute if the try box code fails with syntax error
except:
    print("Other type of Exception !!!!!!")
else:                                               #only execute if the try box code passes
    print("No Exception occured !!!!!!!!")
finally:                                            #exceute irrespective of try box passes/fails
    print("This will occured everytime")


# Example 4 : one more example of use of try,except,finally,else

def Even_odd():
    try:
        num1=int(input("Enter a number"))
        if num1%2==0:
            print("This is even number")
        else:
            print("This is odd number")
    except:
        print("This is Except line")                    #only execute if the try box code fails
    else:
        print("This is line in else")                   #only execute if the try box code passes
    finally:
        print("This is line in finally")                #exceute irrespective of try box passes/fails

Even_odd()


#Example 5 : Rising our own exception
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