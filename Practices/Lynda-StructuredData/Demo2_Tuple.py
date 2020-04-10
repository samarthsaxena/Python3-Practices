#!/usr/bin/env python3

def main():
    game = ('Rock','Paper','Scissors','Lizard','Spock')
    print(game[1:5:2])
    # game.append('Hello')     #it's an error because tuple is an immutible object
    index_of_item = game.index('Spock')
    print(f'Index of item : spock is : {index_of_item}')
    print_list(game)

def print_list(arg1):
    print(f'Lenght of list is : {len(arg1)}')
    for item in arg1:
        print(item, arg1.index(item))

if __name__ == '__main__':
    main()
