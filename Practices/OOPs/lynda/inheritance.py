#!/usr/bin/env python3

#Using self instead of self
class Animal:
    """ Demo class for constructor"""
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs:self._sound = kwargs['sound']

    # Below are the methods serving as setter and getter
    def type(self, t=None):
        if t:
            self._type = t
        try: return self._type
        except AttributeError: return None

    def sound(self, t=None):
        if t:
            self._sound = t
        try: return self._sound
        except AttributeError: return None

    def name(self, t = None):
        if t:
            self._name = t
        try: return self._name
        except AttributeError: return None

# This allows the print method to be overriden
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

def main():
    kitten_1 = Kitten(type='kkkkk', name='Fluffy', sound='rawr')
    duck_1 = Duck(type='DDDDDD', name='Donald', sound='Quackkkk')
    print(kitten_1)
    print(duck_1)
    print(Animal(type=None,sound='',name=''))

    #Calling kill method of Kitten class
    kitten_1.kill("This guy")


if __name__ == '__main__':
     main()
