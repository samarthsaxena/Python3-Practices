#!/usr/bin/env python3

person = {'name': 'Samarth', 'age':24}

sentence_1 = "My name is  {0} and I'm {1} years old".format(person['name'],person['age'])

print(sentence_1)

sentence_2 = "My name is  {1} and I'm {0} years old".format(person['name'],person['age'])

print(sentence_2)

# sentence_3_wrong_arg = "My name is  {1} and I'm {2} years old".format(person['name'],person['age'])
#
# print(sentence_3_wrong_arg)
