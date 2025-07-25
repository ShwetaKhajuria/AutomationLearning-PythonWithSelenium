#Approach 1 - you can import everything but you need to specify module name everytime
import Caluclator
Caluclator.add(10,50)
Caluclator.mul(10,50)

#Approach 2 - you can import specific functions and no need to specify module name everytime
from Caluclator import add,mul
add(50,60)
mul(50,50)

#Approach 3- imports everything and you dont need to specify the module name everytime you try to access something
from Caluclator import *
add(90,90)
mul(90,90)

