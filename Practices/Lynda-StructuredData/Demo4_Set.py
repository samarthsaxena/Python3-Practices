#!/usr/bin/env python3

#Set ia just like List
#But it does not allow duplicates


def main():
    a = set("We're gonna need a bigger boat")
    b = set("I'm sorry Dave, we can't do that..")
    print('set a : ',a,'\n set b : ',b)

    print_set(sorted(a))
    print_set(b)
    print_set(a - b)
    print_set(b - a)
    print_set(a | b)
    print_set(a ^ b)
    # print_set(a + b)


def print_set(o):
    print('{', end = "")
    for x in o:
        print(x,end='')
    print('}')



if __name__ == '__main__':
    main()
