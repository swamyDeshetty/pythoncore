#Program to check whether the number is prime or not

num=int(input('enter the number:'))

for i in range(2,num):
    if num%i==0:
        print('it is not a primenumber')
        break
else:
    print('it is primenumber')


#program to check the primenumbers from 1 to 100

n = int(input('Enter the number:'))

for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)