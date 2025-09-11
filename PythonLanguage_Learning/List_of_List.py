
My_ListofList = [[4,8],[5,6,7],[6,9,10]]
mylist=[1,2,3]

#Access one number 7 from the list
print(My_ListofList[1][2])

#Sum all the numbers from the list
result=0
for k in My_ListofList:
    for l in k:
        result+=l
print(result)

#Create a plain list of all the elements
EMPTY_LIST=[]
for i in My_ListofList:
    for j in i:
        EMPTY_LIST.append(j)
print(EMPTY_LIST)