#!/usr/bin/env python3

def main():
    animals = { 'kitten':'Meow',
                'puppy':'roooff',
                'lion':'grrrrr',
                'giraff':'I am a giraff',
                'dragon':'rawrrr'}
    print('-------------print_dict-----------------')
    print_dict(animals)
    print('-------------boolean_check-----------------')
    boolean_check(animals)


def boolean_check(args_dict_1):
    print(f'kitten in the dictionary: {"kitten" in args_dict_1.keys()}')
    print('Kitten' in args_dict_1.keys())
    print('grrrrr' in args_dict_1.values())
    print('grrrrR' in args_dict_1.values())

    #Checking with one liner code
    print('Checking with one liner code')
    print('Found' if 'kitten' in args_dict_1.keys() else 'Not Found!')
    print('Found' if 'Kitten' in args_dict_1.keys() else 'Not Found!')
    print('Found' if 'I am a giraff' in args_dict_1.values() else 'Not Found!')
    print('Found' if 'I am a girafF' in args_dict_1.keys() else 'Not Found!')


def print_dict(arg_dict):

    #Gives keys
    for key in arg_dict:
        print(f' {key}   ->    {arg_dict[key]}')    #Access through []
        print(f' {key}   ->    {arg_dict.get(key)}')    #Access through get() method

    print('------------------------------')

    #Gives tuples e.g. ('kitten', 'Meow')
    for i in arg_dict.items():
        print(i)

    print('------------------------------')

    #Gives pair of Keys and Values
    for key, value in arg_dict.items():
        print(f'{key} --relates to-> {value}')

    print('------------------------------')

    #To get Keys out of the passed object
    for key in arg_dict.keys():
        print(f'Key in dict object : {key}')

    print('------------------------------')

    #To get values out of the passed object
    for valu in arg_dict.values():
        print(f'Value in dict object : {valu}')

if __name__ == '__main__':
    main()
