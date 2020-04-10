'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'Global x'
y = 'Gloal y'
def test():
    y = 'Local y'
    x = 'Local x'
    print(y)
    print(x)

test()
print(y)
print(x)
