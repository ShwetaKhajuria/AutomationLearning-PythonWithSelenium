def sumofdigits(s):
    sum1=0
    for digit in str(s):
        sum1+=int(digit)
    return sum1

s=input("Enter a number for sum of digits:")
finalsum=sumofdigits(s)
print("sum of digits - ",finalsum)