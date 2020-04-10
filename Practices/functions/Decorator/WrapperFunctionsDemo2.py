#!/usr/bin/env python3

def f1():
    print('from f1')
    def f2():
        print('from function f2..')
    return f2


x = f1()

x()
