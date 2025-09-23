# Iternables dundermethod - __itr__() -> iter(obj)
# Iterators  dundermethod - __next__() -> next(obj)

nums = [4,5,6,7]

# Ex- List,dictonary,string,tupes ect are iterables
# Iterables - something that can be looped over for example
for num in nums:  # This means iterables
    print(num)


# How to find if something is iterables
print(dir(nums)) # if  __iter__ is available that means its iterable,
                 # dir function is used to see whats available

# How to find something is iterator - it will have next method
# print(next(nums)) ### "TypeError: 'list' object is not an iterator"
# for num in nums:
#     print(next(num)) ### "TypeError: 'int' object is not an iterator" the it will not know the next value


#How do we create our iterables List into iterators , it will go forward and no backwords
i_num=iter(nums)
print(next(i_num))
print(next(i_num))
print(next(i_num))
print(next(i_num))


#Real life example - Use of Iterators (generators-yield) to create range a like function
def read_Iter(start,end):
    current=start
    while current<end:
        yield current
        current+=1

for n in read_Iter(5,11):
    print(n)