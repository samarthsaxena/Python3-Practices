student = {'name' : 'Samarth','age' : 25,'courses': ['Math','CompSci']}



#to know how many keys are there, simply use len method
print(len(student))


#to know all the keys
print(student.keys())

#to know all the values
print(student.values())

#to know keys and values together
print(student.items())




#looping through keys
for a in student:
    print(a)
    
for a in student.keys():
    print(a)


for b in student.values():
    print(b)


#to loop through keys and corresponding values
for key, value in student.items():
    print(key, value)
