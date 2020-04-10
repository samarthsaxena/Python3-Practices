#! /usr/bin/env python3


import sys


def inclusive_range(*args):
    """
    Generator function
    using exception handling
    :param args:
    :return:
    """
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1 :
        raise TypeError(f'Expected at least 1, got {numargs} args')
    elif numargs > 3:
        raise TypeError(f'Expected at most 3, got {numargs} args')
    elif numargs == 1:
        stop = args
    elif numargs == 2:
        start , stop = args
    elif numargs == 3:
        start ,stop , step = args
    else:
        raise TypeError(f'Got {numargs} args')

    #generator
    i=start
    while i <= stop:
        yield i
        i += step

def main():
    try:
        for i in inclusive_range(4,25,2,3):
            print(i, end='\t')
    except TypeError as t:
        print(f'{t}')
        print(f'{sys.exc_info()}')
        print(f'{sys.argv}')
        print(f'{sys.getfilesystemencoding()}')


if __name__ == '__main__':
    main()