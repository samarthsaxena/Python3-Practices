#   *args refers to tuple
#  **kwargs refers to dictionary

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)


student_info()
print('-----------------------')
student_info('Math','CompSci',name='Samarth', age=24)
print('-----------------------')


courses = ['Math', 'CompScience']
info = { 'name' : 'Samarth', 'age' : 24}

student_info(courses,info)
print('-----------------------')
student_info(*courses,**info)