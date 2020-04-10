#!/usr/bin/env python3

# here the number is formated by using the ','
#We can also specify the ndecimal places.
sentence1 = '! MB is equal to  {:,} bytes.'.format(1000**2)
sentence2 = '! MB is equal to  {:,.3f} bytes.'.format(1000**2)
print(sentence1)
print(sentence2)
