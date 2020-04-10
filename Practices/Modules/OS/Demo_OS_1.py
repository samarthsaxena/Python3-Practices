#!/usr/bin/env python3

import os

print(dir(os))

print("Current Directory where we're working in : ", os.getcwd())

print(' CD to new directory : ')

os.chdir('/')
print(os.getcwd())

print("Let's see what are the contents of this directory")
print(os.listdir())
print("Total items in this : ",len(os.listdir()))

print("Let make some directories")
#mkdir()   :  to create only one Directory
#makedirs()  :  to create directory heirarichy. nested directories
os.makedirs('dir-1\sub-dir-1')
print(os.listdir())
print("Now let's rmove what we created ")
#rmdir() : to remove specific Directory
#removedirs() : to remove everything recurively
os.removedirs("dir-1\sub-dir-1")
# os.removedirs("dir-2\sub-dir-2")
