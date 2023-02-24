# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1		
	yield 2		
	yield 3		

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

# A Python program to demonstrate use of
# generator object with next()

# A generator function
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# x is a generator object
x = simpleGeneratorFun()




# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))


#program to find the fibonacci series..
def fib(limit):
	
	# Initialize first two Fibonacci Numbers
	a, b = 0, 1

	# One by one yield next Fibonacci Number
	while a < limit:
		yield a
		a, b = b, a + b

# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
	print(i)


#another fibonacci example...
def facto(num):
    a,b=0,1
    while a<num:
        yield a
        a,b = b,a+b #here is the actual logic  there
n=int(input('Enter your number'))
x=facto(n)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#iterating using the for loop
for i in facto(n):
    print(i)