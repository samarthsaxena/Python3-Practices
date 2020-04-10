#!/usr/bin/python3


class Node:
    """
    Class to generate the Nodes at will
    """
    def __init__(self, datavalue = None):
        self.datavalue = datavalue
        self.next = None


def main():
    input_val = list(map(int, input("Value : ").split()))
    size_of_input = len(input_val)

    print("Total inputs entered : ",size_of_input)

    root_node = Node
    temp = root_node
    for item in input_val:
        temp_node = Node
        temp_node.datavalue = item
        temp.next = temp_node

    for i in size_of_input:
        print(i,'-',root_node.datavalue)



if __name__ == '__main__' :
    main()

