# Customize string representation of an object

# object.__str__(self)
# object.__repr__(self)
# object.__format__(self, format_spect)
# object.__bytes__(self)

class Person(object):
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # TODO: use __repr__ to create a string for debugging
    def __repr__(self):
        return "<Person class: fname:{0}, lname:{1}, age:{2}".format(
            self.fname, self.lname, self.age
        )

    # TODO: Usr str for more readability
    def __str__(self):
        return "Person ({0} {1} is {2})".format(
            self.fname, self.lname, self.age
        )

    # bytes conversion
    def __bytes__(self):
        val = "Person: {0}:{1}:{2}".format(
            self.fname, self.lname, self.age
        )
        return bytes(val.encode('UTF-*'))


def main():
    # Create a person object
    person = Person()

    # use different python functions to convert object to string
    print(repr(person))
    print(str(person))
    print("Formatted {0}".format(person))
    person_bytes = bytes(person)
    print(f'{person_bytes}')  # b'Person: Joe:Marini:25'

    print("After decoding")
    print(f'{person_bytes.decode(encoding="UTF-8")}')


if __name__ == '__main__':
    main()
