first_name ="Shweta"
last_name = "Khajuria"

# format strings before 3.6 (old method)
print("My name is {} {}".format(first_name,last_name))

# New F method
print(f'My name is {first_name} {last_name}')


# Capitalized first and last string
print(f'My name is {first_name.upper()} {last_name.upper()}')

# use of f string with dictionary
person={"name":"Shweta","age":"42"}
print(f"My name is {person['name']} and my age is {person['age']}")

# use of f string with calculation
print(f'4 multiply by 11 is {4*11}')

# use of f string with for loop
for n in range(1,11):
    print(f'double of {n:02} is {n*2:.2f}') #:02 is padding 0 in front of n and :.2f is adding 2 digits after .

# use of f string on birthday
from datetime import datetime
birthday=datetime(1984,5,11)
print(f'My birthday is on {birthday:%B %d %Y}')

