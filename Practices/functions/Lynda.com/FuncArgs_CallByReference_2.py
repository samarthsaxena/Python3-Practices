#!/usr/bin/env python3


#Remember : 1.Integers are immutible objects so when you manipulate the object, the copy will be manipulated but the original
#           2.Since list is an mutible object so it's referce is passed.


#Demo 2 of call by reference in python3

def main():
    x = [5]
    y = x

    print(id(x),f'----->   {x}')
    print(id(y),f'----->   {y}')

    y[0]= 3
    print("-------------------")
    print(id(x),f'----->   {x}')
    print(id(y),f'----->   {y}')

#Driver code goes here
if __name__ == '__main__':
    main()
