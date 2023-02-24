#program to find the min and max number:

a=[4,2,3,0,8]

min=a[0]
n=len(a)
for i in range(1,n):
    if a[i]<min:
        min=a[i]
print("The minimum no is",min)

#max number: 

a=[4,6,2,1,5]

max=a[0]
n=len(a)
for i in range(1,n):
    if a[i]>max:
        max=a[i]
print(max)





#swapping of 2 numbers:

def outer(func):
    def inner(a,b):
        print('a value before swapping',a)
        print('b value is before swapping',b)
        a,b=b,a
        func(a,b)
    return inner
@outer
def decorator(a,b):
    print('a value after swapping',a)
    print('b value is after swapping',b)

decorator()

