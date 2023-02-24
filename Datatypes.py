#Data types in python..
#list..
a=[1,2,3,4,5,6]
a.append(10)
print(a)
a.remove(4)
print(a)
a.insert(2,10)
print(a)
print(a.count(2))
print(len(a))
print(type(a))
#print(a.replace(1,11))
print(a[3])#indexing
print(a[2:4])
#tuple..
b=(1,2,3,4,5,6)
print(b[0])
print(b[1:4])
#dictionery
c={'name':'swamy','age':22,'color':'red'}
print(c.keys())
print(c.values())
#set
#collections of unrodered elements is called the set
#set wont allow duplicates
#set is mutable
#set is declared in the flower brackets{}
a={1,2,4,5,2,4,6,7,89,0,5}
print(a)
a.add(10)
print(a)
a.clear()
print(a)
a.add(5)
print(a)
a.add(3)
a.add(5)
print(a)
a.remove(5)
print(a)
