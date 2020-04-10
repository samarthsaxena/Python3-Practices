#!/usr/bin/env python3

def f1(f):
    print('In f1')
    def f2():
        print('In f2 before calling the function')
        f()
        print('In f2 after calling the function')
    return f2

#This is called Decorator
#Meaing: Wrapping up a function inside of another
#So here f3 is actually wrapped inside of function f1()
@f1
def f3():
    print('In f3 ')

# It's like implementing the Decorator, but there's a shortcut for This in line 14 with @
# f3 = f1(f3)


def main():
    f3()

if __name__ == '__main__':
    main()
