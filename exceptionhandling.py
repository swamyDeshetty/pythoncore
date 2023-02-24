#python program to handle simpleruntimeerror

a=[1,2,3]

try:
    print('second element',(a[1]))

    #Throws error since there are only 3 elements in list
    print('fourth element',(a[3]))

except IndexError:
    print('error occured')

a=3
 
try:
    if a<4:
        b=a/a-3 #it raises the zero division error.
    
    print(b) #if a>4 then it arises the name error
except (ZeroDivisionError,NameError):
    print('Error occured and handled..')

#Run time error

a=2
b=0

try:
    print(a/b) 

except Exception:
    print("Hey you can't divide the 2 by 0")

#we can also print the error name...

a=5
b=0
try:                      #first it tries if any error occures it terminated to the except block
    print(a/b)
except Exception as e:    #exception give us the what type of error we gott..
    print('the error is')
    print(e)
finally:                  #finally block will executes if error occures or not
    print('Error is handled..') 



a=3
b=5

try:
    a=int(input('enter the number'))
    print(a)
except Exception as e:
    print(e)
finally:
    print('Error is handled')