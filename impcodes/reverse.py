#program to find it is an palindrome or not

#first need to reverse the string

a=input('Enter the string:')
reverse=''

for i in a:
    reverse=i+reverse
print(reverse)

if a==reverse:
    print('it is an palindrome string')
else:
    print('it is not palindrome')



#program to check the number is palindrome or not
n=135
reverse=0
while n>0:
    num=n%10
    reverse=reverse*10+num
    n=n//10
print(reverse)