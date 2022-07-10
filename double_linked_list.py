# Double-linked-list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list():
    def __init__(self):
        self.head = None

    def push(self, val):
        NewNode = Node(val)
        NewNode.next = self.head
        if self.head != None:
            self.head.prev = NewNode
        self.head = NewNode

    def list_print(self, node):
        while (node != None):
            print(node.data)
            last = node
            node = node.next

double_l_list = doubly_linked_list()
double_l_list.push('None')
double_l_list.push(8)
double_l_list.push(16)
double_l_list.push(24)

double_l_list.list_print(double_l_list.head)


