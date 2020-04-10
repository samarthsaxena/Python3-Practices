#!/usr/bin/env python3

def f1(f):
    def f2():
        print('Thisi is before the function call')
        f()
        print('this is after the function call')
        # retrun 0
    return f2

def f3():
    print('this is f3')

#Passing f3 as an argument to f1
x = f1(f3)

x()
print("--------------------")
# Here we're not actually creating a wrapper,
#As we can see that the f3() is easily beaing called
f3()
