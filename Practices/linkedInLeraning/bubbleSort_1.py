#!/usr/bin/env python3

def bubble_sort(elements_list):
    print(f'{elements_list} is to be sorted.')

    for i in range(len(elements_list)-1, 0, -1):
        for j in range(len(elements_list)-1):
            if elements_list[i] < elements_list[j]:
                temp = elements_list[j]
                elements_list[j] = elements_list[i]
                elements_list[i] = temp
    return elements_list





def main():
    elems = [2,5,3,7,1,8,10]
    print(f'{bubble_sort(elems)}')

if __name__ == '__main__':
    main()
