# #functions in python

def function(fname,lname):
    print("my firstname is "+fname+' '+"my lastname is "+lname)
function('swamy','patel')

# some more functions
def is_prime(n):
	if n in [2, 3]: #this list contains the all the primenumbers ......[2 to infinite]
		return True
	if (n == 1) or (n % 2 == 0):
		return False
	r = 3
	while r * r <= n:
		if n % r == 0:
			return False
		r += 2 
	return True
print(is_prime(18), is_prime(19))

#python code check whether the number is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
n=int(input("enter the number:"))
evenOdd(n)

#default arguments
def add(x=10,y=20):	
	print(x+y)
	print(y*x)
add(27,28) #if we give any arguments here it will take this only and not consider the default arguements....

def add(x,y=10):
	print("the value is the ",x)
	print("the default value is the",y)
add(26)

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
 
 
# Keyword arguments
student(firstname='swamy', lastname='patel')
student(lastname='patel', firstname='swamy')


# Python program to illustrate
# *args for variable number of arguments
 
 
def myFun(*argv):
	
	for i in argv:
		print(i)
 
 
myFun('Hello', 'Welcome', 'to', 'Hyderabad')

def myfun(*args):
	for i in args:
		print( "welcome to ",i)
myfun('chennai')
# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
	for i in kwargs.items():
		print("%s == %s" % (i))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

def myFun(arg1, **kwargs):
	print(arg1)
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='swamy', mid='patel', last='Deshetty')

def myname(**kwargs):
	for i in kwargs.items():
		print("%s == %s" % (i))

myname(name='swamy',cast='patels')


def myFun(x):

	# After below line link of x with previous
	# object gets broken. A new object is assigned
	# to x.
	x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def myFun(x):
 
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20
 
 
# Driver Code (Note that lst is not modified
# after function call.
x = 10
myFun(x)
print(x)


# Python code to illustrate the cube of a number
# using lambda function


def cube(x): 
	return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))


def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

#lambda function..
#program to check the number is even or odd number...
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))

def cube(y):
	print(f"Finding cube of number:{y}")
	return y * y * y


lambda_cube = lambda num: num ** 3

# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))
