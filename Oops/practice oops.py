#init function 
#__init__function is the reserved method in  the python classes and it is called when the obj is created and it is also called as the constructor.

class school:

    #properties
    x='swamy'
    y='manusha'

    def names(self):
        print('my name is the',self.x)
    def __init__(self) -> None: #init function is the reserved method in the pythonclasses and it is called when the object is created and it is also called as constructor..
        print('my angel name is',self.y) #self is the default parameter it is used to access the properties inside the function..

obj=school()

print('in my college my name is',obj.x)
obj.names()