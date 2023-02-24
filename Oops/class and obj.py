#oops defination..
"""OOPS=>object oriented programming is programming paradigsm that uses the classes and objects in programming .it aims to implement the realworld entities
like inheritance,polymorphism,encapusulation,,..that main concept of oops it is used to bind the data and the functions together as the single unit
so no other part of the code  can access this data.. """

#class def:
'''
*class is the collections of objects
*class is the logical entity that contains attributes and methods
*class is created by the keyword class
*variables are the attributes that belong to the class 
*variables are always public and can be accesed using .dot operator.'''

class student:
    name1='swamy'
    name2='manusha'

    def __init__(self): #this is the init function and the init function is the reserved method in the python classes .it called when the object is created and it also called as the constructor..
        print('This is the init function',self.name1) #accesing the attribute inside function..

    def names(self):
        print('My name is ',self.name1)
        print('Her name is',self.name2)

#creating the obj

obj=student()

print(obj.name1)
print(obj.name2)
obj.names()

#class and instance variables..
# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog

class ssc:
    
    teacher='Manoj'

    def __init__(self,age,color):
        self.age=age
        self.color=color

obj = ssc(21,'white')
obj2 =ssc(25,'black')
print(obj.age)
print(obj.color)
print(obj2.age)
print(obj2.color)
print(obj.teacher)
print(ssc.teacher)


# Python3 program to show that we can create
# instance variables inside methods

# Class for Dog


class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed):

		# Instance Variable
		self.breed = breed

	# Adds an instance variable
	def setColor(self, color):
		self.color = color

	# Retrieves instance variable
	def getColor(self):
		print(self.color)


# Driver Code
Rodger = Dog("jujubi")
print(Rodger.breed)  #this is the instance variable..
Rodger.setColor("Blue")
Rodger.getColor()




class Company:
	attr1='manusha patel'

	def __init__(self,name):
		self.name=name
		print('His name is the unique name that is',name)
		print('His name is the wonderfull name that is',self.name)
		print('she is the beautifull girl in the world and she is talented also innocent girl her name is the ',self.attr1) #accesing the attribute inside the function

obj=Company('swamypatel')

print(obj.attr1)
print(obj.name)
#the main advantage of the constructor is executed without calling it..


class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name
		print(name)
		
	def speak(self):
		print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog("chami")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()

class ssr:

	def __init__(self,name):
		self.name=name
	def setcolor(self,color):
		self.color=color
		print(self.color)
	# def getcolor(self): we can use the instance variable like this also
	# 	print(self.color)

obj=ssr('manu')
print(obj.name)
obj.setcolor('white')
# obj.getcolor()


class TCS:
	name1='maneshkumar'
	name2='HarishKumar'

	#init function or construtor method
	def __init__(self,name):
		self.name=name
		print('The tcs first employee name is the ',self.name1)

	
	def setheight(self,height):
		self.height=height #instance variable 
	def getheight(self):
		print("my height in centimeters",self.height)
		print('The tcs second employee name is the ',self.name2)

	#we can use the instance variable inside the function also.
	def color(self,color):
		self.color=color
		print("my favourite color is",color)


obj=TCS('naresh')
print(obj.name)
obj.setheight(167)
obj.getheight()
obj.color('Powderblue')