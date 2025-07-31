My_List = [3,-5,7,12,9,20]
for i in My_List:
    if i< -1:
        continue
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime= False
            break
    if is_prime:
        print(i)


# numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
#
# for num in numbers:
#     if num < -1:
#         continue
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)