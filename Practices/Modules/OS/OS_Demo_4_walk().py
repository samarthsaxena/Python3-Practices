#!/usr/bin/env python3


#walk() generates a traversal
#it's a generator and yields the dir path and the files within the paths


from datetime import datetime as dt
import os

os.chdir('C:\\Users\\sasaxena\\Pictures\\Camera Roll')


for dirpath, dirnames, filename in os.walk('C:\\Users\\sasaxena\\Pictures\\Camera Roll'):
    print('Current Path: ',dirpath)
    print('Directories: ',dirnames)
    print('Files: ',filename)
    print()
