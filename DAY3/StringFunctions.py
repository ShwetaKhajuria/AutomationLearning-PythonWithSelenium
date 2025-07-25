#Four ways to store strings
s="this is string"
t='Welcome'
r=str("By using str")
u=str('single quote')

# Three ways to store strings with no value
v=""
w=''
x=str()

#Immutable or Mutable
print(id(t)) #it will return the memory address of string
t=t+" To Python"
print(id(t))

s = "hello"
# s[1] = "H"  ## This will raise an error, as strings are immutable
print(s)
s = "H" + s[1:]
print(s)

str1="welcome"
print(str1+ " To python")
print(str1* 7)

str1="welcome to the python"
print(str1[1:3])
print(str1[:6])
print(str1[0:])
print(str1[1:-1]) # will remove the last char

print(ord("B"))
print(chr(65))


#max,min and len
print(max("xzyza"))
print(min("abcd"))
print(len("abcd"))

# in  & not in operators
s="Welcome"
print("come" in s ) #True
print("text" in s ) #false
print("come" not in s) #false
print("text" not in s ) #True

#String comparison
print("tie" == "tim") #False
print("tie" != "tim") #True
print("arrow" > "aron") #True. it will check alphabatical order of char
print("arrow" < "aron") #True
print("right" >= "left") #True
print("yellow" <= "brown") #False
print("abc">"") #True

#Testing string functions
s="1welcome"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print(s.isspace())

#searching for substring
s="Welcome to python"
print(s.endswith("thon"))
print(s.startswith("Wel"))
print(s.find("thon"))
print(s.find("new"))
print(s.count("t"))

#Converting strings
s="welcome to PYTHON"

s2=s.capitalize()
print(s2)

s3=s.title()
print(s3)

s4=s.lower()
print(s4)

s5=s.upper()
print(s5)

s6=s.swapcase()
print(s6)

s7=s.replace("welcome to PYTHON","HURREEYYYYYY")
print(s7)

