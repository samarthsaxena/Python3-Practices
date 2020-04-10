#!/usr/bin/env python3

from datetime import datetime as dt
import os

os.chdir('C:\\Users\\sasaxena\\Pictures\\Camera Roll')

print(os.environ.get('Path'))

list_os = []
for items in dir(os):
    list_os.append(items)
    if items == 'environ':
        print('Found')

for i in list_os:
    print(i)

print(len(list_os))
