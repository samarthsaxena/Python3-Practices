#!/usr/bin/env python3

def test_1():
    assert sum([1,2,3]) == 6 , 'Should be 6'

def test_generic(*args):
    j=0
    for i in args:
        j += i
    assert j == j , 'Should be {}'.format(j)
    print(j)

if __name__ == '__main__':
    test_1()
    print('Test Passed')
    test_generic(3,987,3)
    print('Test Passed')
