# For transforming we use functions like map(), filter(), sorted()

def filterFunction(x):
    if x % 2 == 0:
        return False
    return True


def filterFunction2(x):
    if x.isupper():
        return False
    return True


# http://www.python.org/dev/peps/pep-3107/
# Just for fun added the type here
def squareFunction(x: int) -> int:
    return x ** 2


def toGrade(x: int) -> str:
    if x >= 90:
        return "A"
    elif 90 > x >= 80:
        return "B"
    elif 80 > x >= 70:
        return "C"
    elif 70 > x >= 65:
        return "D"
    else:
        return "F"


def main():
    # define some sample sequence to operate upon
    num = [1, 8, 4, 5, 13, 26, 381, 410, 58, 47]
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO : user filter to remove items from the list
    odds = list(filter(filterFunction, num))
    print(odds)

    # TODO : use filter on non-numeric sequence
    lower_case_chars = list(filter(filterFunction2, chars))
    print(f'{lower_case_chars}')

    # TODO : use map to create new sequence of values
    squares = list(map(squareFunction, num))
    print(f'{squares}')

    # TODO : use sorted and map to change numbers to grade
    sorted_grades = sorted(grades)
    grades_letters = list(map(toGrade, sorted_grades))
    print(f'{grades_letters}', end="\t")
    print("")
    for i_tuple in zip(sorted_grades, grades_letters):
        print(f'{i_tuple}')

    # Run
    # if __name__ == '__main__':   # from Python 3 we don't need to include this line.

main()
