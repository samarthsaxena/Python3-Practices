#!/usr/bin/env python3

nums = [1,2,3,4,5,6,7,8,9,10]

#copying each number from the nums list to my_nums1 list
# my_nums1 =[]
# for each_num in nums:
#     my_nums1.append(each_num)
# print(my_nums1)
my_nums1 = [ n for n in nums]
print(my_nums1)


#Copy square of each number from nums to my_nums2
# my_nums2 = []
# for each_num in nums:
#     my_nums2.append(each_num**2)
# print(my_nums2)
my_nums2 = [n**2 for n in nums]
print(my_nums2)
#Now doing the same thing using map + lambda
# my_nums2_map_lambda = map(lambda n : n**2, nums)
# print(my_nums2_map_lambda)

#Copy each even number from num to new my_list
# my_nums_even = []
# my_nums_odd = []
# for each_num in nums:
#     if each_num % 2 == 0:
#         my_nums_even.append(each_num)
#     else:
#         my_nums_odd.append(each_num)
# print(my_nums_even)
# print(my_nums_odd)
my_nums_even = [num for num in nums if num % 2 == 0]
print(my_nums_even)
# Now using filter + lambda function to do the same task
my_nums_even_filter_lambda = filter(lambda n: n %2 ==0, nums)
print(my_nums_even_filter_lambda)


#Make a list of abcd and 0123 in pairs
# my_list_pair = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list_pair.append((letter,num))
# print(my_list_pair[:])
# Now doing the same using list comprehension
my_list_pair = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list_pair)


#Dictionary comprehension
names = ['Bruce', 'Clark', 'Peter','Logan' , 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(f'{list(zip(names,heros))}')   #1 way
# 2nd way
# my_dict_name_hero = {}
# for name, hero in zip(names,heros):
#     my_dict_name_hero[name] = hero
# print(my_dict_name_hero)
# print(my_dict_name_hero.get('Logan'))
#Now with Dictionary comprehension
my_dict_name_hero = {name:hero for name , hero in zip(names,heros) if name != 'Peter'}
print(my_dict_name_hero)



#Set Comprehensions
nums_duplicates = [1,1,2,3,4,4,4,4,5,6,6,7,8,9,9,10,10,10]
# nums_set = set()
# for each_item in nums_duplicates:
#     nums_set.add(each_item)
# print(nums_set)
#Now using set comprehension
nums_set = {n for n in nums_duplicates}
print(nums_set)


#Generator Comprehensions
# def generator_function(numbers):
#     for n in numbers:
#         yield n**2
# my_gen_list = generator_function(nums)
# print(my_gen_list)
# for i in my_gen_list:
#     print(i, end='\t')
#Now using comprehension
my_gen = (n**2 for n in nums)
print(my_gen)
for n in my_gen:
    print(n , end ="\t")
