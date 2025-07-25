#Approach 1
import AModule
import BModule
A=AModule.Animal()
B=BModule.Birds()
A.display()
B.display()

#Approach 2
from AModule import Animal
from BModule import Birds
A=Animal()
B=Birds()
A.display()
B.display()
A.display()
B.display()

