courses = ['History','Math','Physics','CompSci']
courses_2 = ['Art','Education']

#This is nested list
#i.e. a list is inserted inside of another list

#courses.insert(0,courses_2)

#print(courses)
#O/P:    [['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci']

#print(courses[0])
#O/P:    ['Art', 'Education']



courses.extend(courses_2)
print(courses)
print(len(courses))
#o/p
#['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']
#6
