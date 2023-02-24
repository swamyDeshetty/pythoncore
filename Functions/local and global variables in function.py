#local and global variables in function

def f():
    a="manusha is the beautiful girl "  #local variable
    print(a)
    print(b)
b=10
f()
print(b)

# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG' #accesing the global variable inside the function with keyword global s
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)

a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
    #To change the value of a global variable inside a function, refer to the variable by using the global keyword:
    #the global value  a=1 is changed to the 3 because we accesed it into the local variable.. it is changed to the 3
    global a
    a = 3
    print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


# <h1> global keywords<h1>

# global variable
a = 15
b = 10

# function to perform addition
def add():
    global a
    a=5
    global b
    b=14
    print('addition',a+b)
print(a) #the value is 15 because we printed before function cal
add()
print(a) #the value 15 is changed to the 5 be printed after the function cal 



a=15
def change():
    global a
    a= a+5
    print("the value inside the function is the ",a)
change()
print("the value outside the function is the ",a)


# Python program showing a use of
# global in nested function

#Doubt heree..
def add():
	x = 15
	def change():
		global x
		x = 20
	print("Before making change: ", x)
	print("Making change")
	change()
	print("After making change: ", x)

add()
print("value of x", x)


