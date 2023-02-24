# #decorators in python: Decorator is used to modify the function or decorate the function we can add extra features or function to the existing function using the decorator
def login_required(f1):
        def inner(name,is_login):
            if is_login==False:
                print('Kindly login')
                return
            else:
                return f1(name,is_login)
        return inner
    

@login_required
def home(name,is_login):
    print('Hi this is homepage')

@login_required
def orders(name,is_login):
    print('Hi this is orders page')

def about():
    print('Hi this is the about page..')

home('user',True)
orders('user',True)
about()

#Example 2
# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func() #it goes to the hello_decorator and in hello_decorator the function_to_be_used is passed as argument then it will it execute the function_to_be_used function statements..

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()

# # 3rd example..
# # importing libraries
import time
import math

# # decorator to calculate duration
# # taken by any function.

# #code explaination..
# '''1)first it goes to the calculate_time function and executes the whatever the functions are there
# 2)it goes to the inner 1 the time is starts and next func argument is called..
# 3)It goes to the calculate_time it is passed as the decorator then it executes the that decorator function 
# 4)then the factorial function is calls and that  gives that function o/p .. 
# 5)Then it returns the inner1 function and executes the time of execution.. after the execution..
# 6)once again it goes to the inner1 and starts the time -->
# 7)Then goes to the another decorator function def swamy() and executes the factorialof 3.. after the execution
# 8)it returns to the inner1 function it will prints the time of the execution ..
# 9)And lastly it stops its execution 
# 10)Tough one code to understand..  '''

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

# calling the function.
@calculate_time
def swamy(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

# calling the function.
factorial(10)
swamy(3)

#4th example...
def hello_decorator(func):

	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b


# getting the value through return of the function
print("Sum =", sum_two_numbers(1,2))


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

@decor
@decor1
def num2():
	return 10

print(num())
print(num2())

# 5th example..
def div(a,b):
    print("after the division",a/b)


def designdiv(func):

    def inner(a,b):
        if a < b:
            a,b = b,a
        func(a,b)
    return inner

div1 = designdiv(div)
div1(10,20)
#we can call the decorator function like this also..
#designdiv(div)(10,20)


#6th example..
#swapping of 2 numbers

def outer(func):

	def inner(a,b):
		print("a value before swapping",a)
		print("b value before swapping",b)

		if a<b:
			a,b=b,a
		elif a>b:
			a,b=b,a
		func(a,b)
	return inner

@outer
def decorator_function(a,b):
	print('a value after the swapping',a)
	print('b value after the swapping',b)

decorator_function(20,5)



# 7th example..

def outerfunction(func):
    def inner(a,b):
        if a<b:
            a,b  = b,a
        func(a,b)
    return inner

@outerfunction
def subs(a,b):
    print(a-b)

subs(10,20)


# Decorators with parameters..
# Python code to illustrate
# Decorators with parameters in Python

#1st example with the parameters..

def decorator(*args, **kwargs):
	print("Inside decorator")
	
	def inner(func):
		
		# code functionality here
		print("Inside inner function")
		print("I like", kwargs['like'])
		print('I love',kwargs['like'])
		func()
		
	# returning inner function
	return inner

@decorator(like = "geeksforgeeks")
def my_func():
	print("Inside actual function")



#2nd example with the parameters..

def outer(*args,**kwargs):
    print('this is the another decorator function')
    def inner(func):
        print('This is the inner function')
        print('MY name is',kwargs['like'])
        func()
    return inner

@outer(like='Swamy Patel')
def thisisorgin():
    print('It is completed its execution..')

#Third example
def decorator_func(x, y):

	def Inner(func):

		def wrapper(*args, **kwargs):
			print("I like Geeksforgeeks")
			print("Summation of values - {}".format(x+y) )

			func(*args, **kwargs)
			
		return wrapper
	return Inner


# Not using decorator
def my_fun(*args):
	for ele in args:
		print(ele)

# another way of using decorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')

# Python code to illustrate
# Decorators with parameters in Python (Multi-level Decorators)


def decodecorator(dataType, message1, message2):
	def decorator(fun):
		print(message1)
		def wrapper(*args, **kwargs):
			print(message2)
			if all([type(arg) == dataType for arg in args]):
				return fun(*args, **kwargs)
			return "Invalid Input"
		return wrapper
	return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
	st = ''
	for i in args:
		st += i
	return st


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ


print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))

# Simple recursive program to find factorial
#program to find the factorial..
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)
        #return 5* facto(4) ->facto(4)is the 24
        #5*4 =120
		

print(facto(5))
print(facto(5)) # again performing same calculation


def manu(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1) #facto method is used get the factorial of the number..
n=int(input('enter the number:'))
print(manu(n))