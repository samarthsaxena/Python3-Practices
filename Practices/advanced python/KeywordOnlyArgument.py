# Demo the use of keyword only arguments
import pdb

# Use keyword only argument to help code clarity
def myFunctins(arg1, arg2, *, supressException=False):
    """
     * -> tells that proceeding arguments are "KEYWORD-Only" argument
    :param arg1:
    :param arg2:
    :param supressException: this has to be mentioned while calling this functions
    :return:
    """
    pdb.set_trace()
    print("hello")
    pass


def main():
    # myFunctins(1,2,True)   o/p : TypeError: myFunctins() takes 2 positional arguments but 3 were given
    myFunctins(1, 2, supressException=True)


if __name__ == '__main__':
    main()
