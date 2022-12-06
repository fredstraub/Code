# Find the nth node from the end of a Linked List

# generic constructor for Node data type
from hashlib import new
from platform import node


class Node:
    def _init_ (self, new_data):
        self.data = new_data
        self.next = None

# generic constructor of LinkedList data type
    def _init_ (self):
        self.head = None

    # Constructor of Node and LinkedList
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the nth node from the end of the LinkedList
    def printNthFromLast(self, n):
        temp = self.head

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        if n > length:
            print('Locatoin is greater than the' + ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length -n):
            temp = temp.next
        print(temp.data)