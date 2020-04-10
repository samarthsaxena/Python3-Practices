#!/usr/bin/env python3

#This is called annonymous function
#But you may not be able to call this Function since it doesn't have any name
lambda x : 3*x +1

#So you can assign a name to this lambda expression

#e.g.
g = lambda x : 3 * x+ 1

print(g(7))


#Concating the first and last name
fullname = lambda fname, lname: fname.strip().title()+" "+lname.strip().title()
print(fullname('  SAMartH','   SAXena '))
