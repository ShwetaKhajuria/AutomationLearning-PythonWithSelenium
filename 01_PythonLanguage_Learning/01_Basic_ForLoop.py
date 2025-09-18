# I want to print 1 to 10 numbers individuly with using for loop
print("1 to 10 Numbers")
for i in range(1,11):
    print(i)


print("Even numbers")
for j in range(2,20,2):
    print(j)

print("1 to 10 numbers descending")
for k in range(10,0,-1):
    print(k)


fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)