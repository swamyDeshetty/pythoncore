#polymorphism: Implementing the same thing in the different ways or multipleways..
#writing the function for the numbers and strings it is ex for the polymorphism

a=len([1,2,4,5])
a=len('swamy')

# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z = 0):
	return x + y+z

# Driver code
#same function but no.of arguments are different
print(add(2, 3))
print(add(2, 3, 4))
#polymorphism example..
class India:
    def capital(self):
        print('New Delhi is the capital of India')
    def Currency(self):
        print('Rupee is the currency of India')
class Usa:
    def capital(self):
        print('Washington DC is the capital of USA')
    def Currency(self):
        print('Dollar is the currency of USA')
obj=India()
obj1=Usa()

for i in (obj,obj1):
    i.capital()
    i.Currency()
#Note:Here we used the samemethods in the different classes that means by polymorphism
#implementing the samething in the differentways is called the polymorphism..

#method overloading: a class contains the same methodnames morethan one method and different parameters.. or no of 
#method overloading :A class contains the same method name and different parameters that morethan one method is called the methodoverloading..
# Methodname must be the same and the attributes must not be the same...
class Addition:
    def add(self, a, b, c=None):
        if c is None:
            print(a + b)
        else:
            print(a + b + c)

obj = Addition()
obj.add(10,5)
obj.add(10,4,5)

#method overloading: method name must be the same and the attributes or parameters must not be same..

from multipledispatch import dispatch
class add():
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)
    @dispatch(str,str)
    def add(self,a,b):
        print(a+b)

obj=add()
obj.add(1,2)
obj.add(1,2,3)
obj.add('swamy','patel')

from multipledispatch import dispatch 

class d:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)
    @dispatch(str,str,str,str)
    def add(self,a,b,c,d):
        print(a+b+c+d)
obj=d()
obj.add(10,20)
obj.add(10,20,30)
obj.add('swamy',' ','patel',' ',)











#method overiding: child class overiding the methods of parent class is called the methodoverriding 
#Example 1:
class Bird:
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
	
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
        
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# Example 2:
class Cricket:

    def Batsmen(self):
        print('ABD is the one of the best batsmen in the world')
    def Allrounder(self):
        print('Ravindra jadeja is the one of the best all rounder in the world..')

class Cricket1(Cricket):
    def Batsmen(self):
        print('Statement after overriding the parent method..')
        print('Sachin tendulkar is the best batsmen in the world')
class Cricket2(Cricket):
    def Batsmen(self):
        print('Statement after overriding the parent method..')
        print('Virat Kohli is the one of the best batsmen in the world')

obj1=Cricket()
obj1.Batsmen()
obj1.Allrounder()
obj2=Cricket1()
obj2.Batsmen()
obj2.Allrounder()
obj3=Cricket2()
obj3.Batsmen()
obj3.Allrounder()
    
    
