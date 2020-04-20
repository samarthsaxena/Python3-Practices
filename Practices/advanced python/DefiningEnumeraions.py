# defnine enumerations using Enum base class

from enum import Enum, unique, auto


@unique
class Friut(Enum):
    # name = value
    APPLE = 1
    BANANA = 2
    TOMATO = 3
    ORANGE = 4
    # Enum can NOT contain duplicate keys (its default feature)
    # Enum can contain duplicate values by default but
    # with @unique at Enum class we can impose uniqueness in values as well.

    PEAR = auto()
    # With auto() we can assign the automatic default value which woud start from the last assigned value to a name


def main():
    # TODO : enums have human-readable values and types
    print(f'{Friut.APPLE}')
    print(f'{type(Friut.APPLE)}')
    print(f'{repr(Friut.APPLE)}')

    # TODO : enums have name value property
    print(f'{Friut.APPLE.name} has {Friut.APPLE.value}')

    # TODO : print the auto-generated values
    print(f'{Friut.PEAR.name} is {Friut.PEAR.value}')

    # TODO : enums are hashable, can be used as key
    someDict = {}
    someDict[Friut.APPLE] = "An apple a day, keeps the doctor away..."
    print(f'{someDict}') # o/p: {<Friut.APPLE: 1>: 'An apple a day, keeps the doctor away...'}

if __name__ == '__main__':
    main()
