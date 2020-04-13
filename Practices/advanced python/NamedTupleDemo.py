# demonstrate the usage of namedtuple

import collections as coll


def main():
    """
    For demoing the namedtuple

    Well, so now what are namedtuples? They turn tuples into convenient containers for simple tasks.
    With namedtuples you don’t have to use integer indexes for accessing members of a tuple.
    You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.
    """
    # TODO: create a point namedtuple
    # here "Point" is the name of namedtuple which has 2
    Point = coll.namedtuple("Point", "x y")  # space is used as a delimiter between 2 arguments

    p1 = Point(1, 4)
    p2 = Point("A", 'z')
    print(p1)
    print(p2)

    print("You can get the values just by names as well")
    print(f'p1.x -> {p1.x} and p1.y -> {p1.y}')

    # from https://book.pythontips.com/en/latest/collections.html#namedtuple
    print("from https://book.pythontips.com/en/latest/collections.html#namedtuple")
    Animal = coll.namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")

    print(perry)
    # Output: Animal(name='perry', age=31, type='cat')

    print(perry.name)
    # Output: 'perry'

    print(
        f'perry[0] : {perry[0]}   and length is {len(perry)} which defines total number of attributes/values we can fetch')

    print()
    print("You can use _replace() to change the values of this namedtuple's attributes ")
    p1 = p1._replace(x=1000)
    print("changed namedtuple point p1 ", p1)


if __name__ == '__main__':
    main()
    print()
    print("Useful : when you need a light weight immutability ")
    print("Limitation: You can't use default arg values. "
          "if the data you're working with has large number of optional properties "
          "it is better to stick with basic tuple than the namedtuple")
