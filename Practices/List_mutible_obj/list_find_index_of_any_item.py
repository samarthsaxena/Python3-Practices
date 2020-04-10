courses = ['History','Math','Physics','CompSci']
num = [1,5,2,4,3]

# prints 1  
print(courses.index("Math"))


# I just simply wanna know, if the item is present in the list

#use  in
print('Art' in courses)
print('Math' in courses)

print('--------------------------------------------')

# in  :   also useful in for loops
# for each item it will contact the list and bring it into the loop's code block
#let's look at one simple example
#have many more to come :P
for item in courses:
    print(item)

#Reason why each item is printed in a new line is because, by default print method
#has new line implementation
# if you don't need any new lines added by print(), just use end=''  or end="" as an extra arguement in print()
#example:

print('--------------------------------------------')


for item in courses:
    print(item, end='')
#there're many args available for print, you may wanna look.

