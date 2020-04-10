#!/usr/bin/env python3

import datetime


my_date = datetime.datetime(2018,11,10,12,34,9)

print(my_date) #O/P:   2018-11-10 12:34:09

#Now what if you need to print the date like this
# November10, 2018
#Here's how you can do that

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# Supposee you want to format like this
# November 10, 2018 fell on -- and was the --- day of the years


sentence_1 = "{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} day of the year.".format(my_date)

print(sentence_1)
