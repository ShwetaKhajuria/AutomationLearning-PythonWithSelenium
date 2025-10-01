def find_factorial(num):
    result = 1
    for n in range(1,num+1):
        result=result*n
    return result
print(find_factorial(5))