#program to remove the duplicates from an array

a=[1,4,2,5,8,2,1,4]
numbers=[]
for i in a:
    if i not in numbers:
        numbers.append(i) 
print(numbers)