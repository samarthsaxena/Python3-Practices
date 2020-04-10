courses = ['History','Math','Physics','CompSci']
num = [1,5,2,4,3]

courses_str = ' - '.join(courses)

print (courses_str)

new_list_courses_str = courses_str.split(' - ')
print(new_list_courses_str)
