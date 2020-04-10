#!/usr/bin/env python3

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, $ {} )'.format(self.name,self.age,self.salary)

e1 = Employee('Carl' , 23 , 700000)
e2 = Employee('Sarah' , 26 , 900000)
e3 = Employee('John' , 25 , 100232)


employee = [e1, e2, e3]

def e_sort(emp):
    return emp.salary

s_employees = sorted(employee, key=e_sort, reverse=True)
print(s_employees)
