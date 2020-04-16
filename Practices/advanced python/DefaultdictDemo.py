# demo the usage of deafultdict object
import inspect


def conventionalWayWithDictionary(fruits_param_list: list) -> dict:
    inspect_stack_util()

    # define a list of items that we want to count
    fruits = fruits_param_list
    print(f'Got a list of items {fruits}')
    # use dictionary to count each element
    fruitCounter = {}

    # Count the elemenets in the list
    for fruit in fruits:
        # This is the logic to check if the key is already present
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:  # Else add the key counter to 1
            fruitCounter[fruit] = 1

    # print the result
    for key, value in fruitCounter.items():
        print(f'{key} :{str(value)}')

    return fruitCounter


"""
O/p:
apple :2
pear :1
orange :1
banana :3
grape :1
"""


def with_defaultdict_now(fruits_param_list: list) -> dict:
    inspect_stack_util()

    import collections as coll
    # define a list of items that we want to count
    fruits = fruits_param_list
    print(f'Got a list of items {fruits}')

    # use dictionary to count each element
    # int class in defaultdic says: if something is the key then default value is 0 'Zero'
    fruitCounter = coll.defaultdict(int)

    # Count the elemenets in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print the result
    for key, value in fruitCounter.items():
        print(f'{key} :{str(value)}')

    del coll
    return fruitCounter


""" Same Outputs
apple :2
pear :1
orange :1
banana :3
grape :1
"""


def main():
    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']
    x_dict = conventionalWayWithDictionary(fruits)
    y_dict = with_defaultdict_now(fruits)

    # Worst logic ever :D
    print("Comparing them with custom logic")
    for x_key, x_value in x_dict.items():
        if x_key in y_dict.keys():
            print(f'Values are same in both : key {x_key} : {y_dict[x_key]}') if x_value == y_dict[x_key] else print(
                f'Values are NOT same')

    print(f' from custom_defaultdict_default_factory() {custom_defaultdict_default_factory(fruits, 100)}')


def custom_defaultdict_default_factory(fruits_param_list: list, custom_factory_arg: int = 20) -> dict:
    """
    We can add a custome factory for the defaultdict in object.
    e.g. Suppose we need to have a default value in value of the key
    :param fruits_param_list: the list data we want to perform same ops upon
    :param custom_factory_arg: a default or something.. something whic acts as a default factory for the defaultdict obj
    :return: dict object
    """
    inspect_stack_util()

    import collections as coll
    # define a list of items that we want to count
    fruits = fruits_param_list
    print(f'Got a list of items {fruits}')

    # use dictionary to count each element
    # 'lambda : custom_factory_arg' in defaultdic says: if something is the key then default value is 'custom_factory_arg'
    fruitCounter = coll.defaultdict(lambda: custom_factory_arg)

    # Count the elemenets in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print the result
    for key, value in fruitCounter.items():
        print(f'{key} :{str(value)}')

    del coll
    return fruitCounter


def inspect_stack_util():
    print(f'from {inspect.stack()[1][3]}')


if __name__ == '__main__':
    main()
