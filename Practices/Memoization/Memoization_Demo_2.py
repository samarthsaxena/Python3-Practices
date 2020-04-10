#!/usr/bin/env python3

import time

chached_memo = {}

def expensive_opr(num):
    #Implementing Memoization
    if num in chached_memo:
        return chached_memo.get(num)
    else:
        chached_memo.update({num:num**2})

    print("Computing {}...".format(num))
    time.sleep(2)
    return num**2

result = expensive_opr(4)
print(result)

result = expensive_opr(4)
print(result)

result = expensive_opr(3)
print(result)

result = expensive_opr(4)
print(result)

result = expensive_opr(4)
print(result)

result = expensive_opr(4)
print(result)

result = expensive_opr(4)
print(result)

result = expensive_opr(7)
print(result)

print("Cached the below values")
for key in chached_memo.keys():
    print(f'{key} : {chached_memo.get(key)} ')
