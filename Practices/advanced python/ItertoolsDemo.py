# Advanced iteration functions in the itertools module

import itertools as iter
# https://docs.python.org/3/library/itertools.html
import random


def testFunction(x):
    return x < 40


def customeLogicForAccumulate(x, y):
    """
    Custm logic function for accumulate
    :param x: Number
    :param y: Number
    :return: x + y
    """
    print(f'{x, "is not 0: ", x is not 0} and {y, "is not 0: ", y is not 0}')
    if x and y != 0:
        r = x + y
        print(r)
        return r


def main():
    # TODO: Cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = iter.cycle(seq1)
    print(f'It will keep looping endlessly whenever next() is called over a cycle1 which is a \'{type(cycle1)}\'')
    print(next(cycle1))  # Joe
    print(next(cycle1))  # John
    print(next(cycle1))  # Mike
    print(next(cycle1))  # Joe
    print(next(cycle1))  # John

    # TODO : use count to create a simple counter
    count1 = iter.count(100.05, 11.65)
    print(f'{type(count1)} is another way of loopin')
    print(next(count1))  # 100.05
    print(next(count1))  # 111.7
    print(next(count1))  # 123.35000000000001  due to memory leaks
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # TODO : accumulate creates an iterator that accumulates values
    # vals = [i for i in range(10, 51, 10)]
    vals = [10, 20, 31, 40, 50, 40, 30,42]
    acc = iter.accumulate(vals)
    acc_max = iter.accumulate(vals, max)
    print(f' By default accumulate generate the sum but we can change that.')
    print(list(acc))  # [10, 30, 60, 100, 150, 190, 220]
    print(f'Now if we follow func: (_T, _T) -> _T which is the 2nd args of accumulate() we can find min, max etc.. '
          f'from the given sequence')
    print(list(acc_max))
    print(f'If you want to provide a custom implementation you\'d need to add a custom function that accepts 2 args.')
    print(f'For example with customeLogicForAccumulate() ')
    acc_customeLogicForAccumulate = iter.accumulate(vals, customeLogicForAccumulate)
    print(list(acc_customeLogicForAccumulate))

    # TODO : use chains to connect sequences together
    chain_of_words_from_lists = iter.chain(seq1, vals)
    chain_of_letters = iter.chain("AbcDFea", "123244345")
    print(list(chain_of_words_from_lists))  # ['Joe', 'John', 'Mike', 10, 20, 30, 40, 50, 40, 30]
    print(list(chain_of_letters))  # ['A', 'b', 'c', 'D', 'F', 'e', 'a', '1', '2', '3', '2', '4', '4', '3', '4', '5']

    # TODO : itertools provides 2 filtering functions which are dropwhile and takewhile
    # these 2 keep on executing until a condition is met
    print(f'Example for dropwhile and takewhile')
    print("dropwhile: ", list(iter.dropwhile(testFunction, vals))) # dropwhile:  [40, 50, 40, 30, 42]
    print("takewhile: ", list(iter.takewhile(testFunction, vals))) # takewhile:  [10, 20, 31]


if __name__ == '__main__':
    main()
