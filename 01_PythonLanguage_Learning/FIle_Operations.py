
# How to create a new file and write text in it
f = open("C:/Users/khajuria_S/Desktop/PY/TestFiles/My_New_File1.txt","w+")
f.write("This is my new test file\n")
f.write("To find the text\n")
f.write("Hello Shweta\n")


# with Logic - How to search for specific text in a file
f = open("C:/Users/khajuria_S/Desktop/PY/TestFiles/My_New_File.txt","r+")
Lines=f.readlines()
My_flag=False
for line in Lines:
    if "Hello Shweta" in line:
        My_flag=True
        break
    else:
        My_flag=False

if My_flag==True:
    print("Text is available")
else:
    print("Text is not available")

#Pythonic way - How to search for specific text in a file
with open("C:/Users/khajuria_S/Desktop/PY/TestFiles/My_New_File.txt","r+") as f:
    if "Hello Shweta" in f.read():
        print("Text is available")
    else:
        print("Text is not available")
