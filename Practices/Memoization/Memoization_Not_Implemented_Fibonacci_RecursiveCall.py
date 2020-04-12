#!/usr/bin/env python3

# Memoization not implemented

def fibonacci(number: int) -> int:
    if number == 1:
        return 1
    elif number == 2:
        return 1
    elif number > 2:
        return fibonacci(number - 1) + fibonacci(number - 2)


for i in range(1, 101):
    print(i, " : ", fibonacci(i))

# A very serious performance issue exists here without Memoization.
