print("-------------------------------")

print("Here a and b are stored on different location of memory")
a = [1,2,3]
b = [1,2,3]

print(a == b)

print(a is b)

print("a's id : {}  b's id : {}".format(id(a),id(b)))

print(id(a) == id(b))

print("-------------------------------")
print("Here b and c are stored on same location of memory")
print("Why?, because C is just a copy of B and here they are actually sharing the same memory location.")
b = [2,3,4]
c = b

print(b == c)

print(b is c)

print("b's id : {}  b's id : {}".format(id(b),id(c)))

print(id(b) == id(c))

