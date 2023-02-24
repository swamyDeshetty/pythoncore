
#$first class funtions in python..
# Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()



yell = shout #assigning the function to the yell variable...
print (yell('Hello'))
print (yell('swamy'))

# Python program to illustrate functions
# can be passed as arguments to other functions

def shoout(text):
     return text.upper()
def whisper(match):
     return match.lower()
def freeze(hello):
    freeze = hello("hello this is swamy patel")
    print(freeze)

freeze(shoout)
freeze(whisper)

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print (add_15(10))

#Nested functions..

def outer():
    x=10
    print('outer function')
    def inner():
        print("Im accesed the outer function in to the inner function:",x)
    inner()
outer()

#closures..
def outer():
    x=20
    def inner():
        y = 15
        result = x+y 
        return result
    return inner    
a = outer() #outer function data gets the inner function data and the outer  function data...
print(a()) #here the a is returning the inner function reference  
print(a.__name__) #this is for the function name it returns the function name.


def outer():
    msg="swamy"
    def inner():
        print(msg)
    return inner

a=outer()
a()