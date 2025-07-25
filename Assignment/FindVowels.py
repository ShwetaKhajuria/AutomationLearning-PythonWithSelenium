str=input("Enter your 5 char string") # Use text as a variable because str ina keyword which may cause a bug
count=0
for i in range(1,6): #for i in range (len(str))
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
        count=count+1
print("Count is -",count)
#
# if str[::]

# Approch 2
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# Example usage
text = input("Enter a string: ")
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
