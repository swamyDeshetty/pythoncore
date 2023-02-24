#program to find the fibonacci series

def fib(num):
    
    a,b=0,1 
    while a<num:
        yield a
        a,b=b,a+b

n=int(input('enter the number:'))

for i in fib(n):
    print(i)    