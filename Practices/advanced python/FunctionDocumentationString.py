# Demonstrate the use of function doc strings
#PEP 257 - Explains Docstrings
def myFunction(arg1:int, arg2=None) -> None:
    """
    myFunction(arg1: int, arg2=None) -> does not do any thing :P
    :param arg1: expects an integer arg
    :param arg2: expects an object
    :return: None
    """
    print(arg1, " ", arg2)
    return None


def main():
    myFunction(1, list([1,2]))
    print(myFunction.__doc__)
    print(myFunction.__name__)
    print(myFunction.__module__)
    print(myFunction.__annotations__)
    print(myFunction.__class__)
    print(myFunction.__code__)
    print("__defaults__",myFunction.__defaults__)
    print(myFunction.__dict__)
    print(myFunction.__hash__)
    # print(myFunction.__slots__)


if __name__ == '__main__':
    main()
