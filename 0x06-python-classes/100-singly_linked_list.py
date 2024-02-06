#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initializes a node

        args:
            data (int): The data of the node
            next_node (Node): A pointer to the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get/Set the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/Set a pointer to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """Initialize a new singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list

        args:
            value (Node): The Node to insert
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            ptr = self.__head

            while (ptr.next_node is not None and
                   ptr.next_node.data < value):
                ptr = ptr.next_node

            new_node.next_node = ptr.next_node
            ptr.next_node = new_node

    def __str__(self):
        values = []
        ptr = self.__head
        while ptr is not None:
            values.append(str(ptr.data))
            ptr = ptr.next_node
        return "\n".join(values)
