#!/usr/bin/env python3

s = 'this is a long string with bunch of words in it.'

print(s)
print(s.split())
a = s.split

print(a('i'))

b=s.split("i")
b2 = ':'.join(b)
print(b2)
