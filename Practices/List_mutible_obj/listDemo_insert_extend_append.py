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

courses_0 = ['History','Math','Physics','CompSci']
courses_1 = ['Art','Education']

#Results as a nested list at last
courses_0.append(courses_1)
print(courses_0)
#o/p: History', 'Math', 'Physics', 'CompSci', ['Art', 'Education']]
print(courses_0[len(courses_0) - 1])
print(courses_0[-1])
