#!/usr/bin/env python3

import os as o
from datetime import datetime as dt

o.chdir('C:\\Users\\sasaxena\\Pictures\\Camera Roll')


# stat() method returns a tuple containig attributes of the file
for file in o.listdir():
    mod_time = o.stat(file).st_mtime
    print(file, '  :  ',dt.fromtimestamp(mod_time))
    # if o.stat(file).st_size == 0:
    #     print('zerooooo')


for file1 in o.listdir():
    print(o.stat(file1))
    for constants in o.stat(file1):
        print(constants)
    # print(o.lstat(file1).st_size)
