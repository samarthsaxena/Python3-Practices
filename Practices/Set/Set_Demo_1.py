#un-ordered, no-duplicates,immutible


courses_set = {'History','Math','CompSci','Physics', 'Math'}
print(courses_set)
print(len(courses_set))
#courses_set[0] = 'Art' #TypeError: 'set' object does not support item assignment


#check if Math is a member of this set
print('Math' in courses_set)
