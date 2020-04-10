#! /ur/bin/env python3

import sys


def main():
    try:
        # x = int('foo')  # gives ValueError
        x = int(input('Enter an integer value for x :'))
        y = int(input('Enter an integer value for y :'))

        result = x / y

    except ValueError:
        print('I caught a value error')
    except:
        """Default except"""
        print('SOme error came')
        print("Error information is given by python sys module(sys.exc_info()): ")
        print("{}".format(sys.exc_info()))

    #if no error arises then else block ii=s executed
    else:
        print("Good Job !!")
        print(f'{x} / {y} = {result}')


if __name__ == '__main__':
    main()