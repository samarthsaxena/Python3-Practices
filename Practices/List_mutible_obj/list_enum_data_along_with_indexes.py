courses = ['History','Math','Physics','CompSci']
num = [1,5,2,4,3]


for index, course in enumerate(courses):
    print   (index, course)


print(enumerate(courses))

#Suppose you don't want to show that index starts with 0
#So you can specify an extra aurguement in enumeration called 'start' and give it a starting point
#example:

for index, course in enumerate(courses, start=1):
    print   (index, course)
#now instead of printing 0, this prints out 1. that's just the renaming of the index
#i.e. 0 ->1
#     1->2   etc.
    


