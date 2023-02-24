#swapping of 2numbers

def outer(func):
    def inner(a,b):
        print('a value before swapping',a)
        print('b value before swapping',b)
        if a<b:
            a,b=b,a
        elif a>b:
            a,b=b,a
       
        func(a,b)
    return inner

@outer
def decorator(a,b):
    print('a value after swapping',a)
    print('b value after swapping',b)

decorator(7,9)


#Another logic
a=10
b=20
a=a+b
b=a-b
a=a-b
print('After swapping a value',a)
print("After swapping b value",b)