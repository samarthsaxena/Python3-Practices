#!/usr/bin/env python3
#os.path module to combine the Directory with filename to make a full path
#We'd be using os.path.join (to be exact)
#join method actually alaviates the uncertinity of keeping / or \ in the file path
import os

os.chdir('C:\\Users\\sasaxena\\Pictures\\Camera Roll')
print(os.getcwd())

print(os.environ.get('ChocolateyInstall')) # C:\ProgramData\chocolatey

# for dirpath, dirname, filename in os.walk(os.environ.get('ChocolateyInstall')):
#     print(f'Directory path : {dirpath}')
#     print(f'Directory name : {dirname}')
#     print(f'File name : {filename}')

full_path  = os.path.join(os.environ.get('ChocolateyInstall'), 'Demo_1.txt')
print(full_path)  #C:\ProgramData\chocolatey\Demo_1.txt

#What if you wanna know whether  this path exists
#Use os.path.exists() method
print(os.path.exists(full_path))  #False

#Now if you neeed just the basename i.e. the file name with it's type
#use os.path.basename()
name_1 = os.path.basename(full_path)
print(name_1) #Demo_1.txt
print(os.path.exists(name_1))

# Now if have full path of the file like /tmp/temp/test.txt
#And you need just the path of the file
#use os.path.dirname()
name_2 = os.path.dirname(full_path)
print(name_2)  #C:\ProgramData\chocolatey
print(os.path.exists(name_2))


#Now if you need to split the Directory name and file name in separate variables
#use os.path.split() method
dir_file_set = os.path.split(full_path)
print(dir_file_set," <-- ",type(dir_file_set))



#What if you need to know the root of the file and know it's extenssion seperately
#Here's what you can use known as os.path.splitext() method
splitext_var = os.path.splitext(full_path)
print(splitext_var) #('C:\\ProgramData\\chocolatey\\Demo_1', '.txt')
print(type(splitext_var)) #<class 'tuple'>
a= set(full_path.split('.'))# this gives a set, but not so wise if used
print(a)


#functions and things available in os.path module
print(dir(os.path))
