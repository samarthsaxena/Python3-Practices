#!/usr/bin/env python3

#Not a Closure
def outer_function():
    message = 'Hello'

    def inner_function():
        print(message)

    #This is called executing the function, whe you actually use () after function name
    return inner_function()



if __name__ == '__main__':
    outer_function()
