x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

#https://stackoverflow.com/questions/1261875/python-nonlocal-statement#1261961
# nonlocal statement is used for handling the variables in decorators and classes and functions
#global statement is used for handling the top lavel variable manipulations
