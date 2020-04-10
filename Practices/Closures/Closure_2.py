 #!/usr/bin/env python3

def outer_function():
    message = 'Hello'

    def inner_function():
        print(message)

    #This is called returning a function, whe you DO NOT use () after function name
    return inner_function


my_func = outer_function()   # here my_func is a function now and equals to inner_function
                            # wanna know more ? ans: print it with __name__
print(my_func.__name__)    #O/P:    inner_function


#Closure: it's an inner function that remembers and has access to vars in the local scope where they're executed
#even after outer function has executed completely

#Here we may call inner_function function by simply calling my_func function
my_func()

my_func()

my_func()

my_func()

my_func()

my_func()
