#!/usr/bin/env python3
import time
import math

"""
Improvement 1:
---------------
This Function utilizes the number theory
if there's a number N, then it's factors can be arrenged as below
N = 1 * N                          --
  = ...                              |
  = a * b                            |      Group 1
  = (N)^1/2  * (N)^1/2             --|
  = b * a                            |      Group 2
  = ...                              |
  = N * 1                          --

  So we can calculate if any number is prime with help of Group 1
  We really need not to check for the Group 2, since it's having the same set of factors; just in reversed order.
"""

"""
Improvement 2:
-------------

Calculating primes for even numbers are waste of time, since we already know primes are always odd numbers except 2
2 is even and prime as well

So we must eleminate the checks for even numbers
and restricting our function to check for only odd numbers.
"""
def is_a_prime_number(n):

    """ Checks if n is a prime number. Returns true if n is a prime, otherwise false."""

    # Since 1 is not a prime number
    if n == 1:
        return False

    # 2 is already a prime number
    if n == 2:
        return True

    # eliminate check for even numbers
    if n >2 and n % 2 == 0:
        return False

    # Now check only of odd numbers
    max_number_check = math.floor(math.sqrt(n))

    # adding a step of 2 will ensure we're working with odd numbers. e.g. 3   3+2=5, 5+2 = 7  etc.
    for i in range(3, max_number_check + 1, 2):
        if n % i == 0:
            return False
    return True


    # if n <= 0 throw an error
    if n <= 0:
        print("Can not calculate prime.")
        return

#Also check for the time complexity
t0 = time.time()
#Test function
j= 1000001
for d in range(1,j):
    is_a_prime_number(d)   # time complexity : 0.13914728164672852
    # print(d,'  is_a_prime_number : ', is_a_prime_number(d))

t1 = time.time()

print("Time taken for ", j, " Primes: ", t1 - t0)
