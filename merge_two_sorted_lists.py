"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class Node():
    def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def addToList(self, data):
        new_node = Node(data)
        if self.head != None:
            current = self.head
            while current.next != None:
                current.next = new_node
        else:
            self.head = new_node

    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next


list1 = LinkedList()
# list2 = LinkedList()
list1.addToList(1)
list1.addToList(2)
list1.addToList(4)

# list1.addToList(1)
# list1.addToList(3)
# list1.addToList(4)

list1.printList()


