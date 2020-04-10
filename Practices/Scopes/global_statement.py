x = 'Global x'
y = 'Gloal y'
def test():
    global x
    y = 'Local y'
    x = 'Local x'
    print(y)
    print(x)

test()
print(y)

#Here you're able to access variable x, since it's set to global scope at line 3 in function test()
print(x)
