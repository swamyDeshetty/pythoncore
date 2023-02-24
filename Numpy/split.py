#spliting arrays in multiple splits

# import numpy as np
# a=np.array([1,2,3,5,7   ])
# b=np.array_split(a,2)
# print(b)
# for i in a: #we can access th splits like this also
#     print(i)

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# b=np.array_split(a,2)
# print(b)


import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 2)

print(newarr)

#spliting using the axis..
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array_split(a,4,axis=1)
print(b)

x=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array_split(x,3,axis=1)
print(y)

p=np.array([[1,2],[3,4],[5,6]])
q=np.array_split(p,2,axis=1)