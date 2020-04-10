#!/usr/bin/env python3

class Animal:
    """ Demo class for constructor"""
    def __init__(self,**kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Kiiitten_DEFAULT'
        self._name = kwargs['name'] if 'name' in kwargs else 'FFLLUFFFFYYYY_DEFAULT'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'RaWRRRRR_DEFAULT'

    def type(self, t = None):
        if t :
            self._type = t
        return self._type

    def sound(self, t = None):
        if t:
            self._sound = t
        return self._sound

    def name(self, t = None):
        if t:
            self._name = t
        return self._name

    def __str__(self):
        """
        This is a special method that represent the print
        :return:
        """
        return f'the {self.type()} is named {self.name()} and says {self.sound()}.'

def main():
    a0 = Animal(type='Kitten', name='Fluffy', sound='rawr')
    a1 = Animal(type='Duck', name='Donald', sound='Quackkkk')
    #here try changing the type name or sound using the class methods
    a0.sound('Bark')

    #Not recommended to do so. always use getter and setter methods.
    a0._name = 'Barkkkk'

    print(a0)
    print(a1)

    #The Animal() shows the default values assigned by __init__() of class Animal
    print(Animal())

if __name__ == '__main__':
     main()
