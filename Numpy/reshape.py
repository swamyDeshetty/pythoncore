#converting the 1d array to the 2d and 3d arrays

import numpy as np

a=np.array([1,2,3,4,5,6,7,8])
b=a.reshape(2,4)
print(b)

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(2,3,2)
print(y)

#converting the 2d array to the 1d array..
#flattening arrays

z=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
k=z.reshape(-1) #converting from 3d array to the 1d array
print(k)

x=np.array([[1,2],[3,4]])
p=x.reshape(-1) #converting from 2d array to the 1d array
print(p)