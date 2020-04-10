student = {'name' : 'Samarth','age' : 25,'courses': ['Math','CompSci']}


print(student)

# del will delete the matching key-value from dictionary
del student['age']


print(student)



#pop will delete the key value and return what value got deleted

name = student.pop('name')

print(name)
print(student)
