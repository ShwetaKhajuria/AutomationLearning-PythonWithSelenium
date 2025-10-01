# Print numbers 1 to 50, but:
# Print "Fizz" for multiples of 3
# Print "Buzz" for multiples of 5
# Print "FizzBuzz" for multiples of both.

for n in range(1,51):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)

