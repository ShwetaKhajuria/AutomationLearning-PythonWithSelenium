#           Formula - ["expression" for "a value" in "iterable" if "condition"]

# EX1:-     Filter words by length
#           From ["cat", "elephant", "dog", "tiger"], get only words longer than 3 letters.
#           👉 ["elephant", "tiger"]
words = ["cat", "elephant", "dog", "tiger"]
bigger_words=[word for word in words if len(word)>=4]
print(bigger_words)

# EX2:-      Multiples of 3
#            Get numbers from 1–50 that are divisible by 3.
My_list = [num for num in range(1,51) if num%3==0]
print(My_list)


# EX3:-      Flatten a nested list
#            From [[1, 2], [3, 4], [5, 6]], get [1, 2, 3, 4, 5, 6].
# simple_list=[]
# for n in list_into_list:
#     for j in n:
#         simple_list.append(j)
# print(simple_list)
list_into_list = [[1, 2], [3, 4], [5, 6]]
simple_list1=[j for n in list_into_list for j in n ]
print(simple_list1)


# Ex4:-      Word length mapping
#            From ["apple", "banana", "cherry"], get [5, 6, 6]..
fruit_list=["apple", "banana", "cherry"]
num_list=[len(n) for n in fruit_list]
print(num_list)



