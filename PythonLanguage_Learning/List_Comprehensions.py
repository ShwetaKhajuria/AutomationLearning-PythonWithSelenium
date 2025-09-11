# List Comprehension - is a compact way to create a new list
#            Formula - ["expression" for "a value" in "iterable" if "condition"]

# Traditional way to write lists
double=[]
for x in range(1,11):
    double.append(x*2)
print(double)

# List comprehencion
#double = ["expression" for "a value" in "iterable" if "condition"]
sdouble = [y*2 for y in range(1,11)]
print(sdouble)

#List Comprehension