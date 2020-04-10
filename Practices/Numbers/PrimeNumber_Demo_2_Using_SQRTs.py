#!/usr/bin/env python3
import time
import math

"""
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
def is_a_prime_number(n):

    """ Checks if n is a prime number. Returns true if n is a prime, otherwise false."""

    # Since 1 is not a prime number
    if n == 1:
        return False

    max_number_check = math.floor(math.sqrt(n))
    for i in range(2, max_number_check + 1):
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
    is_a_prime_number(d)
    # print(d,'  is_a_prime_number : ', is_a_prime_number(d))

t1 = time.time()

print("Time taken for ",j," Primes: ",t1 - t0)
