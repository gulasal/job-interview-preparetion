#Single Linked List 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)

linked_list.head.next = second_node
second_node.next = third_node
print(linked_list.print_list())

    