# Demonstrate the variable argument list
#https://book.pythontips.com/en/latest/args_and_kwargs.html
# TODO : define a function that takes variable arguement list
def addition( *args):
    number_of_args = len(args)
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # TODO: pass different arguments
    print(addition(10, 12, 3))
    print(addition(10, 0, 3, 12, -1, 5, -4))

    list_of_test_numbers = [temp for temp in range(100, 201, 3)]
    # TODO : pass an existing list
    from_addition_function = addition(*list_of_test_numbers)
    from_manually_adding = 0
    for i in list_of_test_numbers:
        from_manually_adding += i

    # Ternary operator example here
    # https://book.pythontips.com/en/latest/ternary_operators.html
    print("Addition is correct" if from_addition_function == from_manually_adding else "Addition is not working")


if __name__ == '__main__':
    main()
