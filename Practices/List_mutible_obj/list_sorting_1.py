courses = ['History','Math','Physics','CompSci']
num = [1,5,2,4,3]

#sort  in assending order        
courses.sort() 
num.sort()


#sort method actually works on original da
print(courses)
print(num)
#To sort the list without disturbing the original data consider sorted() method
#ex is in lis_sortin_without_disturning_original_data.py
courses_1 = ['History','Math','Physics','CompSci']
num_1 = [1,5,2,4,3]

courses_copy = courses_1
num_copy = num_1

#sort in dessending order
courses_1.sort(reverse = True)
num_1.sort(reverse = True)
print(courses_1)
print(num_1)
print(courses_copy)
print(num_copy)



