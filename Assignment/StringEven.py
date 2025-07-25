# Approach 1- string is given
str='shweta'
for i in range(0,6):
    ch=str[i]
    if i%2==0:
        print(ch)

#Approach 2- when string is asked
str1=input("Enter your string here - ")
ch1=str1[::2]
print(ch1)