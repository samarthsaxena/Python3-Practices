#!/usr/bin/env python3

a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))

print('Before swaping...')
print(f'a: {a}\t\tb: {b}')
print(f'ID of a {id(a)} \t ID of b {id(b)}')


a,b = b,a
print('*' *10)
print('After swaping...')
print(f'a: {a}\t\tb: {b}')
print(f'ID of a {id(a)} \t ID of b {id(b)}')
