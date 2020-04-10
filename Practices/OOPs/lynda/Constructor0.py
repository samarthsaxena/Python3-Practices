#!/usr/bin/env python3

class Animal:
    """ Demo class for constructor"""
    def __init__(self,type,name,sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def sound(self):
        return self._sound

    def name(self):
        return self._name

def print_info(obj):
    """ Printing information about Animal object"""
    if not isinstance(obj, Animal):
        raise TypeError('Required Animal Object')

    print(f'the {obj.type()} is named {obj.name()} and says {obj.sound()}.')

def main():
    a0 = Animal('Kitten','Fluffy','rawr')
    a1 = Animal('Duck','Donald','Quackkkk')
    print_info(a0)
    print_info(a1)
    # print_info(Animal())


if __name__ == '__main__':
     main()
