courses = ['History','Math','Physics','CompSci']
num = [1,5,2,4,3]

courses_str = ', '.join(courses)
#join method actually take each item from the list and make a string literal while
#formating it with other string. in our case ', '  a comma and a space

print(courses)
print(courses_str)
print(courses_str[0])


courses_str_temp = '* * *'.join(courses)
print(courses_str_temp)
