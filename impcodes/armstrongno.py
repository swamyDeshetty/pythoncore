#python code to check the number is armstrong or not

#The sum of cubes of each digit is equal to the number itself..
#when each of its digits is raised to the power of the number of digits in the number.
num=input('Enter Your number ')
temp=int(num)
n=len(num)
sum=0
while temp>0:
    sum+=(temp%10)**n   
    temp=temp//10

if sum==int(num):
    print(int(num),'is an armstrong number')
else:
    print(int(num),'is not an armstrong number:')


#armstrong number

num=input('Enter the number:')
temp=int(num)
n=len(num)
sum=0
while temp>0:
    sum+=(temp%10)**n
    temp=temp//10

#checking the condition.
if sum==int(num):
    print('it is an armstrong number')
else:
    print('it is not an armstrong number')