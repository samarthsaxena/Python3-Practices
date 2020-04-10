student = {'name' : 'Samarth','age' : 25,'courses': ['Math','CompSci']}

print(student.get('name'))
print(type(student.get('name')))


#if accessing with non-existing key
#get method returns None , with no errors
print(student.get('nnnn',"Nahi mila je nnnn"))

print(type(student.get('nnnn')))
