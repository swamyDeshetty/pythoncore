#for loops in python
#For loop is used for iterating over the sequence..
a=[1,2,3,4,5]
n=len(a)
for i in range(0,n):
    print(i)

a=["swamy","patel","shiva","prasad"]
for i in a:
    print(i)


for i in range(10):
    if i%2==0:
        print("even number",i)
    else:
        print("odd number",i)