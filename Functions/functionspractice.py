#functions in py

def fun(fname,lname):
    print('my firstname is',fname,'mylastname is',lname)

fun('swamy','patel')

def check(x):
    if(x%2==0):
        print('even number')
    else:
        print('odd number')

n=int(input('enter the number:'))
check(n)

#in functions we have the 4types of aguments..
# 1)Normal arguments

def func(fname,lname):
    print(fname,lname)
func()
















# # 2)Default arguments
   
# def func(x=4,y=10):
#     return x+y

# print(func())
# print(func(10,20)) #if we give the parameters then it will takes the lastgiven parameters it ignores the default..
  




# # 3)Keyword arguments

# def func(fname,lname):
#     print(fname,lname)
# func(fname='swamy',lname='patel')

# # 4)Variable length arguments

# def fun(*args):
#     for i in args:
#         print(i)
# fun('manusha','patel')

# # 5) keyword arguments

# def fun(**kwargs):
#     for i in kwargs.items():
#         print('%s == %s'%(i))
# fun(name='swamy',age=22)



# #first class functions
# #in firstclass functions the firstclass functions can be assigned to variable and functions can return the another functions
# # function can be assigned as variable//

# def fun(text):
#      return text.capitalize()
#      return text.upper()
# man=fun

# print(man('nareshpatel'))

# #functions can be passed as the arguments to the another function 

# def fun(man):
#     return man.upper()
# def fun2(hello):
#     return hello.lower()
# def fun3(text):
#     fun3=text('manusha')
#     print(fun3)

# fun3(fun)
# fun3(fun2)

# #functions can return another functions

# def outer():
#     x=20
#     def inner():
#         y=10
#         result=x+y
#         return result
#     return inner
# print(outer())
# # print(a())

# #functions can be assigned as parameter to anotherfunction

# def hello(text):
#     return text.upper()
# def trest(hero):
#     return hero.capitalize()
# def phone(mi):
#     phone=mi('My phone is good')
#     print(phone)
# phone(hello)
# phone(trest)

# #functions can return another functions

# def outer():
#     x=20
#     def inner():
#         y=15
#         result=x+y
#         return result
#     return inner
# a=outer()
# print(a())


#Decorators
#Decorators are used to modify behaviour of function.we can add the extra features or functions to the existing function using the decorator

def outerfunction(func):

    def wrapper_function():
        print('inside the wrapper function..')
        func()
        print('After executing the Decorator')
    return wrapper_function

@outerfunction
def decorator_function():
    print('This is the decorator')
# x=outerfunction(decorator_function)
# x()
decorator_function()

import time
import math
def calculate_time(func):
	
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
	def inner1(*args, **kwargs):

		# storing time before function execution
		begin = time.time()
		
		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)

	return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

@calculate_time
def swamy(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

# calling the function.
factorial(10)
swamy(3)


#Decorator is used to modify the behaviour of the function.we can add extra features or functions to the existing function using the decorator

def outer_function(func):

    def inner_function():
        print('This is before the decorator')
        func()
        print('After the decorator function')
    return inner_function

def function_to_be_used():
    print('This is the decorator function')

x=outer_function(function_to_be_used)
x()



#decorator function
#program to find the factorial


def outerfunction(func):

    def inner(*args,**kwargs):

        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        print('Time of execution',end-start)
    return inner

@outerfunction
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))

factorial(5)



# def outer(func):

#     def inner():
#         x=func()
#         return x*x
#     return inner

# def outer1(func):
    
#     def inner():
#         y=func()
#         return y+y
#     return inner

# @outer
# @outer1
# def dec():
#     return 10

# print(dec())

# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner


@decor1
@decor
def num():
	return 10

# @decor
# @decor1
# def num2():
# 	return 10

print(num())
# print(num2())

#swapping of two numbers..

def outer(func):

    def inner(a,b):

        if a<b:
            a,b=b,a
        elif a>b:
            a,b=b,a
        func(a,b)
    return inner
@outer
def dec(a,b):
    print("a value is",a)
    print("b value is",b)

dec(10,5)




a=55
b=10
a,b=b,a
print("a value is ",a)
print("b value is ",b)



#decorator with the arguments.. 

def decorator(*args,**kwargs):

    def inner(func):
        print('I love',kwargs['like'])
        func()
    return inner

@decorator(like='geeks for geeks')
def function():
    print('this is the normal')


#program to find the factorial of number

def function(num):
    
    if num==1:
        return 1
    else:
        return num * function(num-1)
print(function(5))

