#!/usr/bin/env python3

x ='Global x'

def outer():

    x = 'Outer x'
    def inner():
        x ="Inner x"
        print(x)
    inner()
    print(x)
outer()
print(x)
