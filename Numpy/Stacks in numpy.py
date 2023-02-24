#Normal stack:

#1d array
import numpy as np 
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.stack((a,b)))
print(np.stack((a,b),axis=1))

#2d array
a=np.array([[1,2,4],[4,5,6]])
b=np.array([[11,22,23],[5,6,7]])
print(np.stack((a,b)))
print(np.stack((a,b),axis=1))

#c stack:
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.column_stack((a,b)))

# c stack 2d array
a=np.array([[1,2,4],[4,5,6]])
b=np.array([[11,22,23],[5,6,7]])
print(np.column_stack((a,b)))

#h stack:
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.hstack((a,b)))

#2d array
a=np.array([[1,2,4],[4,5,6]])
b=np.array([[11,22,23],[5,6,7]])
print(np.hstack((a,b)))

#v stack
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.vstack((a,b)))


#2d array
a=np.array([[1,2,4],[4,5,6]])
b=np.array([[11,22,23],[5,6,7]])
print(np.vstack((a,b)))








