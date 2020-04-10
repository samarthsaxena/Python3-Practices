#!/usr/bin/env python3

def main():

    #To test stop
    for i in inclusive_range(25):
        print(i, end=" ")
    print()

    #to test start and stop
    for i in inclusive_range(1,25):
        print(i, end=" ")
    print()

    #to test start, stop and step
    for i in inclusive_range(1,25,5):
        print(i, end=" ")
    print()

    #to test random length of args
    for i in inclusive_range(0,25,0):
        print(i, end=" ")
    print()



#Creating own range function i.e. an example of generators
def inclusive_range(*args):
    numargs = len(args)

    #default vaues for starting point and how ti increment with step
    start = 0
    step = 1

    # initialize the parameters
    if numargs < 1:
        raise TypeError(f'Expected atleast 1 arguement, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start,stop, step) = args
    else:
        raise TypeError(f'Expected at most 3 args, got {numargs}')

    #really generator is just these 4 lines of code
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
    main()
