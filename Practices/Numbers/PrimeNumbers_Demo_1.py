#!/usr/bin/env python3
import time

def is_a_prime_number(n):

    """ Checks if n is a prime number. Returns true if n is a prime, otherwise false."""

    # Since 1 is not a prime number
    if n == 1:
        return False

    for i in range(2, n):
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
j= 100001
for d in range(1,j):
    # is_a_prime_number(d)
    print(d,'  is_a_prime_number : ', is_a_prime_number(d))

t1 = time.time()

print("Time taken for ",j," Primes: ",t1 - t0)
