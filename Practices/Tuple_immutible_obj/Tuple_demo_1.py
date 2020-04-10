print("--------------------List Operations go here-------------------------")

list_1 = ['History','Math','Physics','CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)
print("--------------------Tuple Operations go here-------------------------")
tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

print("--------------------Tuple is not mutible, so assignment opr is causing an error here.-------------------------")
tuple_1[0] = 'Art'   # o/p: 'tuple' object does not support item assignment
print(tuple_2)
print(tuple_1)
