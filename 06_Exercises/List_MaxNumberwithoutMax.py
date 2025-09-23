My_List = [20,218,2,8,1,4,235]
largest=My_List[0]
print(largest)
for n in My_List:
    if n>largest:
        largest=n
print(f'This is the Max number is {largest}')
