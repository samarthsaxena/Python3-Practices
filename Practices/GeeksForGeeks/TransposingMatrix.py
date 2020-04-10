#!/usr/bin/env python3

m = [[1,2],[3,4],[5,6]]

#Just to make sure if the matrix is working
for row in m:
    print(row)

#Using list comprehenssions
temp_1 = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
 #[ [ t[i][j] for i in range(len(m)) ] for j in range(len(m[0])) ]

print('\n')

for row in temp_1:
    print(row)



#Now using zip
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
    print(row)
print("\n")
t_matrix = zip(*matrix)
for row in t_matrix:
    print(row)


#Another way is to use numpy package
# import numpy
# matrix_numpy = [[1,2,3],[4,5,6]]
# print(matrix_numpy)
# print(numpy.transpose(matrix_numpy))
