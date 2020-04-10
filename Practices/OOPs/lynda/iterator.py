class inclusive_range:
    """Implementation of Iterator
    This mimics generators to some extent.
    Always a better idea is to use generators inspite of iterators"""

    def __init__(self, *args):
        """ This would check and set all  the args"""
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'Expected at leat 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start,self._stop,self._step) = args
        else:
            raise TypeError(f'Expected at most 3 arguments, got {numargs}')


        self._next = self._start

    def __iter__(self):
        """Simply identifies as iterator"""
        return self

    def __next__(self):
        """Used for proceeding in the rang given by args"""
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r

def main():
    print(f'For inclusive_range(25)')
    for n in inclusive_range(25):
        print(n, end=" ")
    print()

    print("For inclusive_range(4,25)")
    for n in inclusive_range(4,25):
        print(n, end=" ")
    print()

    print("For inclusive_range(4,25,2)")
    for n in inclusive_range(4,25,2):
        print(n, end=" ")
    print()

if __name__ == '__main__':
    main()
