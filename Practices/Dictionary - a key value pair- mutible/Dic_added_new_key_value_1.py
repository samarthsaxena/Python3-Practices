student = {'name' : 'Samarth','age' : 25,'courses': ['Math','CompSci']}
print(student)
#good to use like this if only 1 update is required
student['name'] = 'khakjhdkajhdkjah'
print(student)


#Use update method to update and insert new key value pair at once
#update takes a dictionary as an argument and tries to find existing key in this object
#if key is present then the value will be updated otherwise update is gonna create a key-value pair in this dictionary object


student.update({'name': 'BlaBlaBla','phone': 8989729552})

print(student)

print(type(student.get('phone')))
