# Demo the usage of Counters object
# https://book.pythontips.com/en/latest/collections.html#counter

from collections import Counter as cnt
def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "chad", "Darcy", "frank", "Hannah", "kevin", "james", "malanie", "panny", "steve"]

    # list of students in class2
    class2 = ["Bill", "barry", "candy", "Debbie", "frank", "gabby", "kelly", "james", "joe", "sam", "tara", "ziggy"]

    # TODO : create a Counter for class1 and class2
    c1 = cnt(class1)
    c2 = cnt(class2)
    # TODO: how many students in class1 named james
    print(f'{c1["james"]}')
    # TODO : How many students are there in class1
    print(f'total students in class 1: {sum(c1.values())} '
          f'Is that Correct? {"Yes" if sum(c1.values()) == len(class1) else "No"}')
    # TODO:  Combine two classes (This just to know whats the sum of all objects in totality )
    c1.update(class2)
    print(f'Total students (class1 + class2) :{sum(c1.values()) }')


    #TODO: most common name in class1 and class2
    print(f'So after combining the class1 and class 2. the top 3 most common names are {c1.most_common(3)}')

    #TODO : seperate the classes again
    c1.subtract(class2)
    print(f'After the subtraction class 1\'s top 3 most common names are {c1.most_common(3)}')

    # TODO: What's most common between these 2 classes
    print(f'{c1 & c2}')

if __name__ == '__main__':
    main()