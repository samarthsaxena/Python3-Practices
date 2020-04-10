 #!/usr/bin/env python3

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    #This is called returning a function, whe you DO NOT use () after function name
    return inner_function


hi_func = outer_function('Hi')   # here my_func is a function now and equals to inner_function
                            # wanna know more ? ans: print it with __name__
# print(my_func.__name__)    #O/P:    inner_function
hello_func = outer_function('Hello')

hi_func()
hello_func()
