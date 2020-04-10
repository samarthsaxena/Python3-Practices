#!/usr/bin/env python3

def main():
    x = kitten()
    print(type(x),x)   #gives <class 'NoneType'> None if nothing is returned from kitten function

def kitten():
    print('Meow')
    return dict(x= 42,y = 43, z =44)


if __name__ == '__main__':
    main()
