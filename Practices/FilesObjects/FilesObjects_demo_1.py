#!/usr/bin/env python3

#by default open() will open the file in read mode
#modes are r : read ,w : write ,a : append ,r+ : read and write
f = open('test.txt','r')

# print(dir(f))
# print("-----------")
# for things in dir(f):
#     print(things)
#
# print("-----------")
# print(len(dir(f)))

print(f.name)
print(f.mode)

f.close()
