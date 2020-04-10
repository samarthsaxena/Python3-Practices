# Use iterator functions like enumerator, zip, iter, next
def main():
    # define a list of days in english and french
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "testDay01"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO : Use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    # TODO : iterate using a function and a sentinal
    with open("testfile.txt", "r") as fp:
        # iter takes a callable function as an arguement
        for line in iter(fp.readline, ''):
            print(line)
    # TODO : use regular iterations over days
    for d in range(len(days)):
        print(d + 1, days[d])

    # TODO : using enumerate reduces code and provides a counter
    for itemIndexInArray, enumSteppedValue in enumerate(days, start=int(-7.2)):
        print(f'{itemIndexInArray} -> {enumSteppedValue}')

    # TODO : use zip to combine sequences
    for zipTupleData in zip(days, daysFr):
        # zip function can take any number of iterable args
        print(zipTupleData)
        # The total number of elements in all of the args must match,
        # zip would ignore the extra element from the args provided
        # REASON: The .__next__() method continues until the shortest iterable in the argument sequence is exhausted
        #  and then it raises StopIteration.

    # TODO : now using enumerate and zip together is very useful sometime
    for stepValueByEnumerate, valueTupleByZip in enumerate(zip(days, daysFr), start=1):
        print("@", stepValueByEnumerate, "Day: ", valueTupleByZip[0], " -> ", valueTupleByZip[1], " in French")


# From Python 3 we don't need to add if __name__ == '__main__'
if __name__ == '__main__':
    main()

