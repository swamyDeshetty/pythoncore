#searching the index of the array
import numpy as np

a=np.array([1,2,3,4])
b=np.where(a==4)
print(b)

#even number
a=np.array([1,2,3,4,5,6,7,8])
b=np.where(a%2==0)
b=np.where(a%2==1) #odd number
print(b)

#search sorted
a=np.array([1,2,3,4,5,6])
b=np.searchsorted(a,4)
print(b)

a=np.array([3,4,5,6,7])
b=np.searchsorted(a,5,side='right')
print(b)

#multiple values
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)