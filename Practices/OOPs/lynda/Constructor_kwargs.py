#!/usr/bin/env python3

class Animal:
    """ Demo class for constructor"""
    def __init__(self,**kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']

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
    a0 = Animal(type='Kitten', name='Fluffy', sound='rawr')
    a1 = Animal(type='Duck', name='Donald', sound='Quackkkk')
    print_info(a0)
    print_info(a1)
    print_info(Animal(type=None,sound='',name=''))

if __name__ == '__main__':
     main()
