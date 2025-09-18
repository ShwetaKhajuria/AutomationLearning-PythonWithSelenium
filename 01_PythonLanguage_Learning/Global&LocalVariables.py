# ********************* Example 1 ************************************

Global_var =10 #Global var
def myfun():
    Local_Var =20 #Local var
    print("Global Variable=",Global_var)
    print("Local Variable=",Local_Var)
myfun()
print("Global Variable outside function =", Global_var)

# ********************* Example 2 ************************************
xy=50
def cool():
    xy=60
    print(xy)
cool()
print(xy)


# ********************* Example 3 ************************************
yz=100
print(yz)
def cool2():
    global mn
    mn=500
    yz=200
    print(yz)
cool2()
print(yz)
print(mn)

# ********************* Example 4 ************************************
print("********************* Example 4 ************************************")
op = 700
def cool2():
    global op
    op = 800
    print(op)
#cool2()
print(op)


# ********************* Example 5 ************************************
print("********************* Example 5 ************************************")
def cool3():
    global gb
    gb=200
    print(gb)
cool3()
print(gb)