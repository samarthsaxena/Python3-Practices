#!/usr/bin/env python3

def doll(n):
    print(f'{n} is being calculated..')
    if n >= 1000:
        print(f'Returning {n-3}')
        return n - 3
    else:
        print(f'Returning doll(doll({n+5}))')
        return doll(doll(n + 5))


def main():
    print("Answer is : ", str(doll(84)))


if __name__ == '__main__':
    main()
