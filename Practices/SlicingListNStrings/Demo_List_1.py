#!/usr/bin/env python3

my_list = [10, 20, 22, 30, 43, 54, 64, 73, 83, 99]
#index      0   1   2   3   4   5  6   7    8   9
#-ve index -10 -9  -8  -7  -6  -5  -4 -3   -2   -1

# list[start:end:step]


print(my_list)

print(f'Last element of the list : {my_list[-1]}')

print(f'Slicing from 0 index to 4 : {my_list[0:5]}')   # 5th is the non inclusive index
print(f'Slicing : {my_list[1:-2]}')

print(f'Slicing from 5 index to last : {my_list[5:]}')
print(f'Slicing from 2nd last index to first : {my_list[:-1]}')

print(f'Whole list {my_list[:]}')

# print my_list


#step example

print(f'Step of 2  :  {my_list[2:-1:2]}')
print(f'Step of -1  :  {my_list[-2:2:-1]}')

#print reverse of the list
print(f'reverse of the list : {my_list[::-1]}')
