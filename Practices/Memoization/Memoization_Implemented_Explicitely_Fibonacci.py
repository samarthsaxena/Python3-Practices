#!/usr/bin/env python3

#Here we'd have a dictionary of cached values

#This dict would be our cache
fib_cache = dict()

def fibonacci(n):
    #if the value is present in cache, then return it
    if n in fib_cache:
        return fib_cache[n]
    #Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #Cache the value and then return
    fib_cache[n] = value

    return value

#
# for i in range(1,10001):
#     print(i," : ", fibonacci(i))


with open('test_fibonacci.txt','w') as f:
    for i in range(1,11):
        f.write(str(i)+" : "+str(fibonacci(i))+"\n")
