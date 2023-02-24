#iterating array using the for loop
import numpy as np
a=np.array([[1,2,3],[4,5,6]])

for i in a:
    print(i)
#it is getting in the brackets so i use the another for loop because it is the 2d array

for i in a:
    for j in i:
        print(j)

#iterating the 3d array
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in x:
    for j in i:
        for k in j:
            print(k)

#It is difficult using the for loops n times.. so to overcome this issue we use the nditer

x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in np.nditer(x):
    print(i)

#we have also enumerate function but it gives the index number also..

x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for idx,x in np.ndenumerate(x):
    print(idx,x)



# we have the 3types of iterating function  there are for,nditer,ndenumerate( )

a=np.array([1,2,3,4])
for i in a:
    print(i)
for i in np.nditer(a):
    print(i)
for idx,i in np.ndenumerate(a):
    print("idx giving the index",idx, "i giving the numbers",i)


#there are the 3types of iterating functions we have forloop,nditer,ndenumerate

a=np.array([2,3,4,5])
for i in a:
    print(i)

for i  in np.nditer(a):
    print(i)

for x,y in np.ndenumerate(a):
    print(x,y)