# demo for Deque  (pronounced as deck)

# double ended queue

import collections as coll
import string


def main():
    # TODO: initialise a deque with lower case letters
    d = coll.deque(string.ascii_lowercase)
    # TODO: deque supports the len() function
    print(f'Length of deque of lower case letters {len(d)}')
    # TODO : deque can be iterated over
    for i in d:
        print(f'{i.upper()}', end=" ,")
    print()
    # TODO : manipulate items from either ends
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(f'{d}')
    # TODO : rotate the deque
    print("Rotate op:")
    d.rotate(1)
    print(f'{d}')
    d.rotate(int(len(d)/2))
    print(f'{d}')


if __name__ == '__main__':
    main()
