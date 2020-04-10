x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

#https://stackoverflow.com/questions/1261875/python-nonlocal-statement#1261961
