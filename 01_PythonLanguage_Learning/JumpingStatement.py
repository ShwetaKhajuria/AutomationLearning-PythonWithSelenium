#Break Statement
# Ex- Print 1-10 but if 5 arises then break from the loop
for i in range(1,11):
    if i==5:
        break
    print(i)
print("Program Exited !!!")


#Continue Statement
# Ex- Print 11-20 but if skip 13 and 18 numbers

for j in range(11,21):
    if j==13 or j==18:
        continue
    print(j)


