a=float(input("Enter your first numbers here - "))
b=float(input("Enter your second number here - "))

op=input("Please enter A for Addition, B for Substraction, C for Multiplication and D for Division- ")
if op=='A':
    print("You chose Addition. Your answer is - ", a+b)
elif op == "B":
    print("You chose Substraction. Your answer is - ", a-b)
elif op == "C":
    print("You chose Multiplication. Your answer is - ", a*b)
elif op == "D":
    print("You chose Division. Your answer is - ", a/b)
else:
    print("Please select A,B,C or D in caps")

