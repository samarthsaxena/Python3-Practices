#!/usr/bin/env python3

#Decorator is a function that yields a wrapper function in return


def function_1():
    print('From function_1')

#Since, everything is just an object in python3
#Here variable x is able to receive the value from function_1
x = function_1

#and eventually function_1 can be called by calling x()
x()
print(x)
