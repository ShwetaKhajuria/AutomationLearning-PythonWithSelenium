def my_Fibonacci(num):
    a ,b = 0,1
    for n in range(num):
       print(a)
       a, b = b, a + b

my_Fibonacci(10)
