#!/usr/bin/env python3

person = {'name': 'Samarth', 'age':24}

#Here Dict Object person is passed twice.
sentence_1_naive_approach = "My name is  {0[name]} and I'm {1[age]} years old".format(person,person)
print(sentence_1_naive_approach)
#Here only one person object is passed and the placeholders refer to the same Dictionary object.
sentence_1_good_approach = "My name is  {0[name]} and I'm {0[age]} years old".format(person)
print(sentence_1_good_approach)
