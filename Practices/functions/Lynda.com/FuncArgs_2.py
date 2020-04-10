#!/usr/bin/env python3

def main():
    kitten(5, 6,7)
    kitten('Hello','How','Are you?')
    kitten("My age",'is',24)

    kitten_2('Hell',2,8)
    kitten_2(2.22,'heyooo','')
    kitten_2('Hell')
    kitten_2('Hell',2)
    kitten_2('heyooo',None,None)
    kitten_2(2,,)

def kitten(a,b,c):
    print('Meow...')
    print(a,b,c)

def kitten_2(a, b=1, c=0):
    print('From kitten_2')
    print(a,b,c)

if __name__ == '__main__':
    main()
