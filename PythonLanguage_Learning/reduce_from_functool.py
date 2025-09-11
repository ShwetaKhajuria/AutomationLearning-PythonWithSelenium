from functools import reduce

My_List = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,My_List))