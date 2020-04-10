courses = ['History','Math','Science', 'CompSci']

print(courses)
print(len(courses))

#First item in the list
print(courses[0])

#Last item in the list
print(courses[-1])

#Error in accessing extra
#print(courses[4])
print(courses[:2])
print(courses[0:2])
print(courses[2:2])
print(courses[2:])





#in the end of the list
courses.append('Art')
print(courses)

#insert at specific location

courses.insert(0,'Art')
print(courses)
print("List allows duplicated data")



