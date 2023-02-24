# # # fibonacci series:

# # def function(num):
# #     a,b=0,1
# #     while a<num:
# #         yield a
# #         a,b= b,a+b
# # x=function(20)
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))

# # for i in x:
# #     print(i)


# # def function(num):

# #     if num==1:
# #         return 1
# #     else:
# #         num * function(num-1)
# # print(function(5))

# num=input('Enter the number:')
# n=len(num)
# temp=int(num)
# sum=0
# while temp>0:
#     sum+=(temp%10)**n
#     temp=temp//10

# if sum == int(num):
#     print('it is an armstrong number')
# else:
#     print('it is not an armstrong number')


# #min and max

# a=[3,5,0,4,2,9,1]

# min=a[0]
# n=len(a)
# for i in range(1,n):
#     if a[i]<min:
#         min=a[i]

# print(min)

# #decorator function..

# def function(func):
#     def inner(a,b):
#         print('Before the swapping a value is ',a)
#         print('Before the swapping b value is',b)
#         if a<b:
#             a,b=b,a
#         elif a>b:
#             a,b=b,a
#         func(a,b)
#     return inner

# @function
# def decorator(a,b):
#     print('After the swapping a value is',a)
#     print('After the swapping b value is',b)

# decorator(1,3)

# a=input('enter the string')
# reverse=''

# for i in a:
#     reverse=i+reverse
# print(reverse)

# if reverse==a:
#     print('it is an palindrome')
# else:
#     print('it is not an palindrome')

# #reversing the number
# n=int(input('Enter the number'))

# reverse=0

# while n>0:

#     num=n%10
#     reverse=reverse*10+num
#     n=n//10

# print(reverse)
#prime number or not

n=int(input('Enter the number'))

prime=[]

for i in range(2,n):
    if n%i==0:
        print('it not a prime')
        break
else:
    print('it is a prime')

n=int(input('enter the number:'))

for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime.append(i)
        print(i)
print(prime)

#duplicates
a=[1,5,6,2,4,2,0,1,4,5]
duplicates=[]

for i in a:
    if i not in duplicates:
        duplicates.append(i)
print(duplicates)