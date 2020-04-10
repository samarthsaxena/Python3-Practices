#!/usr/bin/env python3

#Sorting integers based on their magnitude values

li = [-6,-5,-4,1,2,3]

print(li)
print('default sorted on these values: ')
li_s = sorted(li)
print(li_s)

print('Now sorting based on their magnitude')
li_s_magnitud = sorted(li, key=abs) # here befor soring the list it will calculate the absolute values of the list parameters
print(li_s_magnitud)

# this key parameter is extremly useful when you work with objects and
#want to sort the objects with different cretaria. e.g. Eployee class example in same sorting directory
