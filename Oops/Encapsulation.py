# Python program to
# demonstrate protected members

# Creating a base class

#Encapsulation:Wrapping up of data is called the encapsulation....
#Encapsulation is done achieved by the 3 access specifiers
# if we declare the data in private access specifier so no other class can access data and modify the data it can be accessed 
# within the class only..
#if we declare the data in the protected access specifier no other class can access this data except derived class and same class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
        # invoking the parent class attr and method we use the init method and attr..
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)



#protected access modifier..
#in the protected access modifier no other class can access the data except the derived class and the ownclass
#we can also modify tthe data in the protected access modifier 

class parent():

    def __init__(self):
        self._a=10
    
class child(parent):
    def __init__(self):
        super().__init__()
        print('Before modify',self._a)
        self._a=15
        print('after modify',self._a)

obj=child()


#2nd example....
class parent():
	_x=15
	def __init__(self):
		self._a=10 #if we use the variable inside the function we use the self keyword prefix to it
	
class child(parent):
	#invoking the properties and methods of the parentclass
	def __init__(self):
		super().__init__()
		print(self._a)
		print(self._x)

obj=child()

# #private access modifier
# #in the private access modifier we can't access the methods outside the class and the we can't modify the data in the private access modifier..
# class Base():
# 	_a=5
# 	def __init__(self):
# 		self.__b=7

# class child(Base):
# 	#invoking the properties of parentclass
# 	def __init__(self):
# 		super().__init__()
# 		print(self._a)
# 		print(self.__b)

# obj=child()


class testing:
	a=7
	def s(self):
		self.a #self is used to access the variables inside the function..
		print(self.a)
		a=10
		print(a)
obj=testing()
obj.s()
