#! /usr/bin/#!/usr/bin/env python3

def outer():
    x = 'outer x'

    def inner():
        nonlocal x      #nonlocal allows to manipulate enclosing variable within any code block
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
