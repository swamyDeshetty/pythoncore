#initializing the arrays
#zeros():it fills the array with the zeros..
import numpy as np
a=np.zeros([2,3])
print(a)
b=np.zeros([4,5])
print(b)

#ones:it will prints only the one numbers..
a=np.ones([2,4])
print(a)

#full:it fills the numbers whatever we want in the array..
a=np.full([4,3],2)
print(a)
a=np.full([3,6],4)


#rand():it will gets the randomvalue
a=np.random.rand(2,3)
print(a)
b=np.random.rand(4,5)
print(b)

#eye:
a=np.eye(2)
print(a)