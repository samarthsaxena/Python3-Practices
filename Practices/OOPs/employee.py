import sys

class Employee:
    """ A sample employee class """
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def test_method(self):
        pass

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Samarth','Saxena')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()
