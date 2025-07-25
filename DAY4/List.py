# How to create a List
a= [10,30,40,50]
b= ['Name', 'Age', 'Salary']
c= [100,"Shweta","Khajuria",80.63]
d=[]

# How to print List
print("How to print the List")
print(a,b,c,d,"\n")

# How to access items from list
print("How to access items from list")
print(a[0],a[3],a[-2])
print(c[1:4])



#How to read all items
print("\nHow to read all items")
for i in a:
    print(i)


#How to check if particular item is available in the list
#Example 1- with using for
for i in b:
    if i=="Salary":
        print("This word is available")
        break
else:
    print("This word is NOT available")

#Example 1- with using if else only
if 30 in a:
    print("\nYes, its available")
else:
    print("\nNo, its Not available")

#How to find total numbers of items available in the list
print(len(a))

#How to add new items/s in the list [Append() & insert()]
a.append(100)
print(a)

a.insert(2,222)
print(a)

#How to remove items/s from the list [pop(),Del,Clear()]
a.pop(0)
print(a)
del a[0]
print(a)
a.clear()
print(a)

#How to copy items from one list to another
#approch 1 - list function
n=list(a)
print(a,n)

#approch 2 - Copy function
m=a.copy()
print(m)

#How to join items from one list to another
#approch 1 - +
j=a+b
print(j)

#approch 2 - for loop with apend
for k in b:
    a.append(k)
print(a)

#Approch 3 - extend ()
b.extend(a)
print(b)


#Compare List 1 is equal to list 2 or not
lis1=(10,20,30)
lis2=(40,50,60)
if lis1==lis2:
    print("List are same")
else:
    print("List are not equal")




























##************************REVISION*******************************
#How to create a list
a=[10,11,12,13,14]
b=['age',20,'name','Henry']
c=[]

# #How to print a list items
# print(a,b,c)
#
# #How to print specific item from the list
# print(a[1],b[0])
#
# #How to read all items from the list
# for i in a:
#     print(i)
#
# #How to check if perticular item is available in the list
# if "age" in b:
#     print("yes, the word is available")
# else:
#     print("no,the word is not available")
#
# #How to find total number of items in the list
# print(len(a))
#
# #How to add new items in the list
# #Approch 1
# a.append(15)
# print(a)
# #Approch 2
# a.insert(2,"new")
# print(a)

#How to remove items from the list
# a=[10,11,12,13,14]
# b=['age',20,'name','Henry']
# c=[]
# print("original list",a)
# #Approch 1
# a.pop(2)
# print("pop",a)
# #Approch 2
# a.remove(11)
# print("remove",a)
# #Approch 3
# del(a[1])
# print("delete",a)
# #Approch 4
# a.clear()
# print("clear",a)


#How to copy one list to other
#Approch 1 - concatination
# r = a+b
# print(r)
# #Approch 2 - for loop with append
# a=[10,11,12,13,14]
# b=['age',20,'name','Henry']
#
# for s in b:
#     a.append(s)
# print(a)
# print(b)

# a=[10,20,30]
# b=["name","age","salary"]
#
# #Copy two lists
# c=a.copy()
# print("a-",a)
# print("b-",b)
# print("c-",c)
#
# #Join to list
# b.extend(a)
# print("a-",a)
# print("b-",b)
# len("test")



