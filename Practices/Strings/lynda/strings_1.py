#! /usr/bin/env python3

# print('Hello World. '.swapcase())

s = 'Hello World.'
s1 = s.upper()
class MySTR(str):

    def __str__(self):

        """ For reversin the order of the letters"""

        return self[::-1]


# print(s)
# print(MySTR(s))

print(id(s))
# print(id(s1))
print(id(s.upper()))

print(id(s)==id(s.upper()))
