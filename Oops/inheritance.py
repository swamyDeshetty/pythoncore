# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person():

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber #if we declare the variables inside the function then we can call that variables as instance variables.

	def display(self):#accesing the instance variables inside the function..
		print('original name is',self.name)
		print('my id is the ',self.idnumber)

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is ",self.name)
		print("IdNumber: ",self.idnumber)
		print("Post:",self.post)


# creation of an object variable or an instance
a = Employee('SwamyPatel', 1543, 25000, "Python Devloper")

# calling a function of the class Person using
# its instance
a.display()
a.details()

#parent class..

class parent1():

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('my name is the ',self.name)
        print('my age is the ',self.age)

class child1(parent1):
    def __init__(self,name,age): #accesing the properties from the parent class is called the inheritance.. accessing the methods and the properties from the parentclass
        parent1.__init__(self,name,age) #invoking the init function of the parentclass

    def displaynms(self):
        print('my name is',self.name)
        print('my age is',self.age)

obj=child1('swamy',22)
obj.displaynms()
obj.display() #we are calling the methods of the parent class using the child object..



#single level inheritance..
class parent2():

    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
    
    def show(self):
        print('my name is the ',self.name)
        print('my role is the ',self.role)
    
class child(parent2):
    def __init__(self, name, role, salary,age):
        self.age=age
        parent2.__init__(self,name,role,salary) #accessing the properties and methods from the parent class using the inheritance concept
    
    def displaydetails(self):
        print('Emp Name is',self.name)
        print('Emp Role is',self.role)
        print('Emp salary',self.salary)
        print('Emp age',self.age)
obj=child('swamypatel','PythonDev',25000,22)
obj.displaydetails()
obj.show()


class parent3():

    def coding(self,name,age):
        self.name=name
        self.age=age

class child5(parent3):
    def __init__(self, name, age): #whenever we are inherting the methods from parentclass  we use the init function here..
        parent3.coding(self,name,age) #it is used to get the properties from the parentclass 
    
    def output(self):
         print('Age is the',self.age)
         print('Name is the',self.name)

obj=child5('SwamyPatel',22)
obj.output()


#inheritance first example..

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False  


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())


# Python program to demonstrate
# single inheritance
# when a class can be derived from one base class this type of inheritance is called single inheritance.
# In single inheritance,all the features of the base class are inherited into the derived class

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class


class Child(Parent):
	def func2(self):
		print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2() #here without using the parentclass we are calling the method of the parent class using the child class it is the inheritance


# Python program to demonstrate
# multiple inheritance
# when class is derived from the morethan one base class this type of inheritance is called the multiple inheritance
# In multiple inheritance all the features of the base class are inherited into the derived class..

# Base class1
class Mother:
	mothername = 'laxmi'

	def mother(self):
		print(self.mothername)

# Base class2


class Father:
	fathername = "Gangaiah"

	def father(self):
		print(self.fathername)

# Derived class


class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)


# Driver's code
s1 = Son()
s1.parents()
s1.mother()
s1.father()

# Python program to demonstrate
# multilevel inheritance

# Base class


class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class


class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class


class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)


# Driver code
s1 = Son('swamypatel', 'Gangaiah', 'Narsaiah')
s1.print_name()


# Python program to demonstrate
# Hierarchical inheritance
# when more than one derived class is created from the one base class this type of inheritance is called Hierarchical inheritance..


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1


class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# Python program to demonstrate
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1,Student2):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
object.func3()
object.func4()

