#!/usr/bin/env python3

person = {'name': 'Samarth', 'age':24}

sentence = 'My name is {name} and age is {age}'.format(**person)

print(sentence)
