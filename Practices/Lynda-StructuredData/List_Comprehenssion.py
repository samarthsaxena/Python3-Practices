#!/usr/bin/env python3

def main():
    seq =range(11)
    seq2 = [(x, x**2) for x in seq]
    dic = { x : x**2 for x in seq }
    set_1 = {x for x in 'hey hi hello whats up'}
    print_list(seq)
    print_list(seq2)
    print(seq2)
    print(dic)
    print(set_1)


def print_list(o):
    for x in o: print(x, end='')
    print()

if __name__ == '__main__':
    main()
