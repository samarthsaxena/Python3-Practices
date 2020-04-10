#!/usr/bin/env python3

import os

modulename = input('Enter module name correctly : ')
print("You enterd : ", modulename)

filename_for_module = modulename+'_functions.txt'
print("Text File : ",filename_for_module,'\nwill be saved at : ',os.getcwd())

with open(filename_for_module,'w') as f:
    for i in dir(modulename):
        print(i, file=f)

print('Generating ',modulename,' functions in: ',filename_for_module)

# with open(filename)
