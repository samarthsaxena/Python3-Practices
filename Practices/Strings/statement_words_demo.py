#!/usr/bin/python3

"""
Sample String to test with
hello samarath! How're you doing ?

"""

import re

statement = input('Enter a statement: ')
pivot = int(input('Enter the pivot to compare: '))

# Find all words (make a list out of that)and remove the special characters
list_of_words = re.findall(r'\w+\b',statement)
# Print out all the investigated words and their lengths
print(f'The words found: {list_of_words}')
print(f'There are {len(list_of_words)} words in the statement.')

# Make a set out of unique words drom the above list
set_of_unique_words = set(list_of_words)
print(f'Unique words in the set : {set_of_unique_words}')
print(f'Length of the set :{len(set_of_unique_words)}')



# Make an empty Dictionary which will be updated for each word with the length of this word.
dict_of_lengths = dict()

for word in set_of_unique_words:
    # Put word as a key and it's own length as a value
    print(f'Putting {word} in dictionary with length {len(word)}')
    dict_of_lengths.update({word:  len(word)})


# Create a list of words having equal or higher number of length than the pivot
list_of_words_greater_than_pivot = list()

# Now check for the values higher than the pivot in the dictionary and print out the keys as list
for key, value in dict_of_lengths.items():
    if dict_of_lengths[key] <= pivot:
        print(f'Item {key} is being removed from the dict object as this has length of {dict_of_lengths[key]}  <= {pivot}')
        del dict_of_lengths[key]
        print(dict_of_lengths)
    elif dict_of_lengths[key] > pivot:
        print(f'Adding {key} to list')
        list_of_words_greater_than_pivot.append(key)
    else:
        print("Something is fhishy here :P")

print(list_of_words_greater_than_pivot)