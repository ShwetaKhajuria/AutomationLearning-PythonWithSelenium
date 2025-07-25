# How to create a Tuple
My_Tup1 = (10,20,"sal","age")

# How to print a Tuple
print("1) Print a Tuple:- ",My_Tup1)

# How to access indivisual values from Tuple
print("2) Access indivisual values from Tuple:-",My_Tup1[1])
print("3) Range of indexes:-", My_Tup1[0:3])

#How to change the value with using workaround [covert into list and do modification and convert back to tuple]
My_tuple=("apple","banana","cherry")

Mylist=list(My_tuple)
Mylist[0]="ORANGE"

My_tuple=tuple(Mylist)
print("4) Modify value with using workaround",My_tuple)

#How to read all items
for i in My_tuple:
    print(i)

#How to search check if the item is available
if "banana" in My_tuple:
    print("Yes, the value is available")
else:
    print("No, Banana is not available")

#How to find a total number in tuple
print(len(My_tuple))

#Add new items into the tuple - Not possible

#Remove items - Not possible

#Copy one tuple into another
Cop_Tuple = My_tuple
print(Cop_Tuple)

Cop_Tuple1=tuple(My_tuple)
print(Cop_Tuple1)

#Delete the tuple
del (Cop_Tuple1)

#Join/combine Tuple
tup1=(10,20,30)
tup2=(40,50,60)
#Approch 1.a
tup3=tup1+tup2
print(tup3)
#Approch 1.b
tup2=tup1+tup2
print(tup2)


#Compare tupple 1 is equal or not
if tup1==tup2:
    print("tupple are same")
else:
    print("tupples are not equal")

