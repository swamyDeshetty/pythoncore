#Abstruction: Hiding the internal information and showing only the relevant information is called the abstruction
#it can be achieved by the interfaces and abstract class

#abstract class:The class which have abstract methods are called the abstract class 
#Abstract class mustbe imported from the ABC module..
#abstract class will mustbe inherited from the ABC
#objects can't be instantiated to the abstractclass

#Abstruction method: The method which have only the declaration but not have the definition 
#in order to make the method as the abstract method we use the decorator @abstractmethod

#Concrete class : The class which dont have any abstract methods. it will be inherited from the abstract class
#objects can be instantiated to the concrete class

from abc import ABC,abstractmethod

class Abstractmethod(ABC):
    
    @abstractmethod #need to use the decorator to change the method as the abstract method..
    def show(self):
        None
class Concreteclass(Abstractmethod):
    def show(self):
        print('It is the concrete class')

obj=Concreteclass()
obj.show()


# 2nd example..
from abc import ABC,abstractmethod

class abs(ABC):
    @abstractmethod
    def display(self):
        None
class con(abs):
    def display(self):
        print('The data is displayed in the concrete class only')

obj=con()
obj.display()