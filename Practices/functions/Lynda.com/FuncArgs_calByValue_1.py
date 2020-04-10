#!/usr/bin/env python3


#Remember : Integers are immutible objects


#Demo of call by value in python3
#Works as same as any other languages
def main():
    print("in main func")
    x = 5

    print(f'Id of x in main: {id(x)}')
    kitten(x)
    print(f'Id of x in main: {id(x)}')
    print(f'After the function call x is {x}')

#Here only copy of the value is passed
#the object itself
#hence you maintain the integrity of the object reference
def kitten(a):
    #here ids of original X and a are same
    print(f'Id of a in kitten: {id(a)}')
    #But after changing the value of a
    a = 3
    #id also changes
    #funny fact :P
    print(f'Id of a in kitten after changing the value: {id(a)}')
    print('in kitten function.')
    print(a)
    print('Going back to main')

#Driver code goes here
if __name__ == '__main__':
    print("callin Main func")
    main()
    print('main func executed.')
