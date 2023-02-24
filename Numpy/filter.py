import numpy as np
a=np.array([41,42,43,44])
b=a[[True,False,True,False]]
print(b) #it will returns only the true value only..
new=[]
for i in a:
    if i%2==0:
        new.append(True)
    else:
        new.append(False)
newarr=a[new]
print(new)
print(newarr)



import numpy as np
a=np.array([41,42,43,44])

bool=[]
for i in a:
    if i>42:
        bool.append(True)
    else:
        bool.append(False)
print(bool)
newarr=a[bool] #assigning the bool values inside the a 
print(newarr)

#filtering the values in the array..

a=np.array([1,2,3,4,5,6,7,8,9])

boolarray=[]

for i in a:
    if i%2==0:
        boolarray.append(True)
    else:
        boolarray.append(False)
print(boolarray)
even_numbers=a[boolarray]
print("The even number from the array are",even_numbers)




a=np.array([1,2,3,4,5,6,7])

newarr=a%2==0
even=a[newarr]
print(newarr)
print(even)



#filtering the values in the array
a=np.array([1,2,3,4,5])
b=[True,False,True,False,True]
newarr=a[b]
print(newarr) #it will fiter the numbers and prints only True values..

#fitering the even numbers from the array
x=np.array([1,2,3,4,5,6,7])

newarr=[]
for i in x:
    if i%2==0:
        newarr.append(True)
    else:
        newarr.append(False)

print(newarr)
even_numbers_array=x[newarr]
print(even_numbers_array)