#!/usr/bin/env python3

import os

os.chdir("C:\\Users\\sasaxena\\Pictures\\Camera Roll")
print(os.getcwd())

# for i , j, k in os.walk("C:\\Users\\sasaxena\\Pictures\\Camera Roll"):
#     print('Directory Path: ', i)
#     print('Directories : ',j)
#     print('File name : ',k)

print('------------------------------------------------------------------')
for i1 , j1, k1 in os.walk("C:\\Users\\sasaxena\\Pictures\\Camera Roll"):
    print('--------')
    print(f'Directory Path: {i1} ','\t', 'Is a Directory: ',os.path.isdir(i1),'Is a file: ', os.path.isfile(i1))
    print(f'Directories : {j1}')
    print(f'File name : {k1}',)

    for item in k1:
        print(f'{item}',os.path.isfile(item))
    for item_1 in j1 :
        print(f'{item_1}',os.path.isdir(item_1))
