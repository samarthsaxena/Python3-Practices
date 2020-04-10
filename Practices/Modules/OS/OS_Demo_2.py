import os

# print(dir(os))

print(os.getcwd())  #C:\Users\sasaxena\AppData\Local\Programs\Python\Python37\Practices

os.chdir('C:\\Users\\sasaxena')

print(os.getcwd())

print(os.listdir())

# os.removedirs('temp_dir')
#
# os.makedirs('temp_dir')

print(os.listdir())

os.rename('requirements.txt','requirements.txt.Test')
