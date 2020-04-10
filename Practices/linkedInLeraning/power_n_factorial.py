#!/usr/bin/env python3

def power(num,pwr):
    """
    calculate the power of a number. If power is 0 then return 1
    """
    if pwr is 0:
        return 1

    if pwr < 0 :
        return "not supported by this function."

    if num != 0 and pwr >= 0:
        return num * power(num,pwr-1)

def factorial(num):
    """
    calculate factorial of a +ve number
    """
    if num <= 1:
        return 1

    if num > 1:
        return num * factorial(num-1)


def main():
    a = int(input('Value of a : '))
    a_pow = int(input('Value of a_pow : '))
    d = int(input('Value of d : '))

    print('{} to the power {} is {}'.format(a,a_pow,power(a,a_pow)))
    print('Factorial of {} is  {}'.format(d,factorial(d)))


if __name__ == '__main__':
    main()
