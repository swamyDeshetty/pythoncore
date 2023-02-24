#Data types in python..

# b-boolean
# i-integer
# u-integer
# c-complex float
# f- float
# m-timedelta
# M-datetime
# O-object
# S-str
# v-void
# u-unicodestring
import numpy as np
a=np.array([1,2,3,4,5,5])
print(a.dtype)
a=np.array([1,2,4],dtype='S')
print(a.dtype)
a=np.array([1.2,2.4])
b=a.astype('i')
print(b.dtype)

a=np.array([1.34,4.5,4.6])
b=a.astype(int)
print(b.dtype)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
print(x)

#copy

a=np.array([1,2,3,4,5])
b=a.copy()
b[2]=9
print(a)
print(b)

#view
a=np.array([12,23,45,67])
b=a.view()
b[3]=22
print(a)
print(b)