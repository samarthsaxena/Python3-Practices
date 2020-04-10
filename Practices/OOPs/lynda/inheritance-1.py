#!/usr/bin/env python3

class Animal:
    """ Demo class for constructor"""
    def __init__(self,**kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t = None):
        if t :self._type = t
        try: return self._type
        except AttributeError : return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError : return None

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError : return None

    def __str__(self):
        return f'the {self.type()} is named {self.name()} and says {self.sound()}.'


class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'Duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'Kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, killing):
        print(f'{self.name()} is going to kill {killing}!!!')

def main():
    """ Driver function"""
    a0 = Kitten(name='Fluffy', sound='rawr')

    #even if you include type keyword arguement, it'd be deleted by init of this class.
    a1 = Duck(type='Duck', name='Donald', sound='Quackkkk')
    #here try changing the type name or sound using the class methods
    a0.sound('Heloooo')
    print(a0)
    print(a1)

    a0.kill("Humans")

if __name__ == '__main__':
     main()
