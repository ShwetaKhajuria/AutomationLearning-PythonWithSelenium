#
# def is_prime(n):
#     # Prime numbers are greater than 1
#     if n <= 1:
#         return False  # Numbers <= 1 are not prime
#
#     # Step 2: Loop from 2 to square root of the number
#     # If any number divides 'n' evenly, it's not prime
#     for i in range(2, num):
#         if n % i == 0:  # If n is divisible by i
#             return False  # Not a prime number
#
#     # Step 3: If no divisors were found, it's prime
#     return True
#
# # Step 4: Ask the user to enter a number
# num = int(input("Enter a number: "))
#
# # Step 5: Call the function and display result
# if is_prime(num):
#     print(f"{num} is a prime number.")  # If True, print it's prime
# else:
#     print(f"{num} is not a prime number.")  # Otherwise, not prime



















# number= input("Enter your number : ")
# num=int(number)
# if num < 1:
#     print("Number is not a Prime number")
# for i in range(2,num):
#     if num%i==0:
#         print("Number is not a Prime NUmber")
#         break
#     else:
#         print("Number is Prime Number")
#         break

def is_prime(num1):
    if num1<= 1:
        return False
    for i in range(2,int(num1**0.5)+1):
        if num1 % i == 0:
            return False
    return True

number=int(input("Enter your number"))

if is_prime(number):
    print("Number is prime")
else:
    print("Number is not Prime")





