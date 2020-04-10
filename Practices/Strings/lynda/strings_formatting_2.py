#!/usr/bin/env python3

x = 10
y= 20

#named param
print('here, something is {yy} and something is {xx}'.format(xx=x,yy=y))

#ordered param
print("ordered params {1} and  {0}".format(x,y))
print("default order params {} and  {}".format(x,y))

#with space formatting
print('something {0:<5} and {1:>5}'.format(x,y))
print('something {:<5} and {:>5}'.format(x,y))
#with sign and filling zeros
print('something {0:<5} and {1:+5}'.format(x,y))


print('Number formatting**************************')

a = 20 * 1935385026
print('this is 20 * 1935385026 = {:,}'.format(a))
print("if you're europian then you'd use a . (peroid) instead of , (comma)")
print('then  20 * 1935385026 is {:,}'.format(a).replace(',','.'))


#If you need standered number formate
print('this is 20 * 1935385026 = {:.3f}'.format(a))

#binary representation
print('this is 20 * 1935385026 in binary is  {:b}'.format(a))

#from python 3.6  we have f strings with us for formatting the strings
print(f'This is {a}')
print(F'This is {a:.3f}')
print(f'This is {a:b}')
