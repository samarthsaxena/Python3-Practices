#!/usr/bin/env python3

tag = "hl"
text = "This is a headline."

#So the arguement based assignment makes it easier to work with String formatting
#It's Good to use arguements explicitly.

sentence = '<{0}>{1}<{0}>'.format(tag,text)

print(sentence)
