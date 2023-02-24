#joining the two arrays

import numpy as np
a=np.array([[1,2,4],[4,5,6]])
b=np.array([[0,1,2],[5,0,9]])

x=np.concatenate((a,b),axis=1)
print(x)