courses = ['History','Math','Physics','CompSci']

#remove completely deletes the value
courses.remove('Math')

print(courses)


#pop actually removes the last item of the list and returns this item
poped_course = courses.pop()
print(poped_course)
print(courses)
