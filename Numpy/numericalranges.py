#numerical ranges in numpy
#arrange function
from traceback import print_stack
import numpy as np
a=np.arange(0,100,10,dtype=float)
print(a)
b=a.reshape(2,5)
print(b)

#linspace:
a=np.linspace(0,100,10) #it will gives the intervels
print(a)
a=np.arange(0,100,10) #it will give the difference
print(a)