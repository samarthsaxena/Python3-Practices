#!/usr/bin/python3


class Node:
    """
    Class to generate the Nodes at will
    """
    def __init__(self, datavalue = None):
        self.datavalue = datavalue
        self.next = None


n1 = Node('Sunday')
n2 = Node('Monday')
n3 = Node('Tuesday')
n4 = Node('Wednesday')


root = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None

start = root
while start:
    print(start.datavalue)
    start = start.next
