from collections import Counter

My_list = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,5]

#Find how many times each value comes
print(Counter(My_list))

#Find the value which appeared most
My_counter = Counter(My_list)
print("\nThis is the value that most appeared - ",My_counter.most_common(1))

#Find first two values that appeared the most
print("\nFirst two values that appears the most- ", My_counter.most_common(2))

