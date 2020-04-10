#!/usr/bin/env python3

temp = [1]
# with open('test.txt', 'r') as f:
#     #Here reading only first n number of characters of the file
#     f_contents = f.read(51)
#     print(f_contents)

with open('test.txt','r') as f2:
    for i in temp:
        print(f2.read(i))
        temp.append(i+temp[0])
