#!/usr/bin/env python3

import time as t

numbers = set()

def repeated_call_function(num1,num2):
    no_1 = num1
    no_2 = num2
    if no_1 in numbers and no_2 in numbers:
        print('Found in Cache')
        return no_1+no_2
    else:
        numbers.update([no_1,no_2])
        # numbers.update(no_2)

    def inner_function():
        t.sleep(2)
        print('inner_function',no_1 + no_2)

    return inner_function

repeated_call_function(3,3)
repeated_call_function(3,4)
repeated_call_function(4,5)
repeated_call_function(2,3)
repeated_call_function(2,3)
