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

def print_info(animalObj):
    """ Printing information about Animal object"""
    if not isinstance(animalObj, Animal):
        raise TypeError('Required Animal Object')

    print(f'the {animalObj.type()} is named {animalObj.name()} and says {animalObj.sound()}.')

def main():
    a0 = Animal('Kitten','Fluffy','rawr')
    a1 = Animal('Duck','Donald','Quackkkk')
    print_info(a0)
    print_info(a1)


if __name__ == '__main__':
     main()
