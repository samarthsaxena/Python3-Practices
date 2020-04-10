#!/usr/bin/env python3

class Person():
    def __init__(self, name , age):
        self.name = name
        self.age = age

p1 = Person('Samarth', 24)

sentence = 'My name is {0.name} and age is {0.age}'.format(p1)

print(sentence)
