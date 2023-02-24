#program to check the vowels  in a string..

n=int(input('Enter the string'))

vowelslist=['a','e','i','o','u']

vowelscount=0
consonanscount=0

for i in n:
    if i in vowelslist:
        vowelscount+=1
    else:
        consonanscount+=1
print(vowelscount)
print(consonanscount )