#!/usr/bin/env python3

#Using this instead of self
class Animal:
    """ Demo class for constructor"""
    def __init__(this, **kwargs):
        this._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        this._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        this._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    # Below are the methods serving as setter and getter
    def type(this, t=None):
        if t:
            this._type = t
        return this._type

    def sound(this, t=None):
        if t:
            this._sound = t
        return this._sound

    def name(this, t = None):
        if t:
            this._name = t
        return this._name

# This allows the print method to be overriden
    def __str__(this):
        return f'the {this.type()} is named {this.name()} and says {this.sound()}.'


def main():
    a0 = Animal(type='Kitten', name='Fluffy', sound='rawr')
    a1 = Animal(type='Duck', name='Donald', sound='Quackkkk')
    print(a0)
    print(a1)
    print(Animal(type=None,sound='',name=''))


if __name__ == '__main__':
     main()
