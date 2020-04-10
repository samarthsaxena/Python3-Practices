#!/usr/bin/env python3

def main():
    passing_variable_lenght_args('meow','grrr','purrr')

    print("-------------------------------")
    #Lets see with tuple variable being passed
    x = ('meow',3,0.110)
    passing_variable_lenght_args(*x)   #While passing any variable as an arg, just put an *

    print("-------------------------------")
    #Lets see with list variable being passed
    list_1 = ['meow',3,0.110]
    passing_variable_lenght_args(*list_1)

# Here * with the formal parameter is treated to be a variable lenght arguement
#to the function
def passing_variable_lenght_args(*args):    #Naming the variable length arg as *args is in standards
    print(f'Total args received: {len(args)}')
    if len(args):
        for item in args:
            print(item)
    else :
        print('Memememem')


if __name__ == '__main__':
    main()
