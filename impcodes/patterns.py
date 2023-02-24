#right side increment

for i in range(5):
    for j in range(i+1):
        print('*',end=" ")
    print()
    
#right side decrement

for i in range(5):
    for j in range(i,5):
        print('*',end=' ')
    print()

#left side decrement

for i in range(5):
    for j in range(i+1):
        print(" ",end=' ')
    for k in range(i,5):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(i,5):
        print(" ",end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()

#half pyramid..

for i in range(5):
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
print('another')
for i in range(5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,5):
        print('*',end=' ')
    for k in range(i,5-1):
        print('*',end=' ')
    print()


for i in range(5-1 ): 
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,5):
        print('*',end=' ')
    for k in range(i,5-1):
        print('*',end=' ')
    print()

for i in range(6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()