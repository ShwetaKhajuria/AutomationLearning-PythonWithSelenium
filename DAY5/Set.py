MySet={9,5,4}

#************************ How to print ************************
print(MySet)

#************************ How to access items from set ************************
for i in MySet:
    print(i)

#************************ How to check item available in the set ************************
j=input("Enter value")
if j in MySet:
    print("Value is available")
else:
    print("Value is not available")

#************************ How to add items to set - single item - add(),Multiple items - update() ************************
MySet.add("shweta")
print("Original",MySet)

MySet.update(["khajuria","QA"])
print("Check this",MySet)

#************************ How to find the how many items in the set ************************
print(len(MySet))

#************************ How to remove item from the set - remove(), discard() ************************
MySet.remove("shweta")
print(MySet)
MySet.discard("test")
print(MySet)

#************************ How to clear all items from the set collection ************************
MySet.clear()
print(MySet)

#************************ How to delete the set ************************
del(MySet) # Will completely delete the set
#print(MySet)

#************************ How to join to sets union(), Update(), | ************************
MySet1={10,20,30}
MySet2={40,50,60}
#Way 1 by using union function
# MySet3=MySet1.union(MySet2)
# print(MySet3)

#Way2 by using update function
# MySet2.update(MySet1)
# print(MySet2)

#Way 3 by using | operator
MySet3=MySet1|MySet2
print(MySet3)


