#!/usr/bin/env python3

li = [3,6,3,1000,8,0,3,2,56,7,92974,98,98,2,3,23,6,5,7,78,1010,2,1,2,362667,37]
sorted_li = sorted(li)
print('Prints the sorted version of li: ',sorted_li)
print('Original li list remains same, unsorted : ',li)
print("Npw acting on original list and sorting it")

li.sort()
print(li)

#Reverse sorting
li_2 = [3,6,3,1000,8,0,3,2,56,7,92974,98,98,2,3,23,6,5,7,78,1010,2,1,2,362667,37]
li_2_rev_sorted = sorted(li_2, reverse=True)
print('Prints reverse sorted version of li_2: ', li_2_rev_sorted)
print('Original is still : ',li_2)
print('Now original is reversed: ')
li_2.sort(reverse = True)
print('Now original is reversed ', li_2)
