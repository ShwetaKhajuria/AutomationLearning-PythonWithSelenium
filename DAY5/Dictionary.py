#**********************How to create a dictionary *******************
My_dic1 ={"x":101, "y":102,"z":103}
My_dic2 = {
    "Brand":"Honda",
            "Model": "ZZ11",
    "Year": 2023
}


#**********************How to print a dictionary *******************
print(My_dic1)

#**********************How to access items from a dictionary *******************
#Way-1
print(My_dic2["Model"])
#Way-2
print(My_dic2.get("Year"))

#      ************************ How to change values in Dictionary ****************
My_dic2["Year"] = 2025
print(My_dic2)


#      *********************** How to read all items from the Dictionary *************
# for i in My_dic2:
#     print(i) # print only keys
#     print(My_dic2[i]) # print only values

# for i in My_dic2.values():
#     print(i)

for x,y in My_dic2.items(): #print keys along with value
    print(x,y)

# *************************** How to check key exists in the dict or not ************
if "Brand" in My_dic2:
    print("Exists")
else:
    print("Not exists")

# ************************* Total number of items in dictionary ************
print(len(My_dic2))

# ************************* Adding items to the dictionary *********************
My_dic2["Color"] = "Grey"
print(My_dic2)

#************************** How to remove items from dictionary **************
#Way 1
My_dic2.pop("Year")
print(My_dic2)

#Way 2
del My_dic2["Model"]
print(My_dic2)

#************** How to delete the dictionary
del My_dic1

# ****************** How to clear all the values from dictionalry
My_dic2.clear()
print(My_dic2)

#********************* Copying  dictionary
My_dic3 ={"x":101, "y":102,"z":103}
My_dic4 = {
    "Brand":"Honda",
            "Model": "ZZ11",
    "Year": 2023
}
# My_dic3=My_dic4.copy()
# print(My_dic3)

# **************** Add items from two dictionaries
My_dic5={}
My_dic5=My_dic3 | My_dic4
print(My_dic5)

#*******************