#!/usr/bin/env python3

#difference b/z str() and repr()

#str()  gives a nicely readable string that can be printed
#repr() gives an unambigiuous string that can be understood/read/executed as a command
import time

a = time.gmtime()
# a = [1,2,3,4]
b = 'Sample string'
c = 2

print(str(a))
print(repr(a))
print(str(b))
print(repr(b))
print(str(c))
print(repr(c))
