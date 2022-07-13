"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
  

class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        self.head = None
        
  
    
    def printList(self):
        while self.head:
            print(self.head.data, end="->")
            self.head = self.head.next
  
    
    def addToList(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        
        while self.head.next:
            self.head = self.head.next
  
        self.head.next = newNode

def mergeTwoLists(list1, list2):
    if list1 == None:
        return list2
    elif list2 == None:
        return list1
    elif list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else: 
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
list1 = LinkedList()
list2 = LinkedList()
list1.addToList(1)
list1.addToList(2)
list1.addToList(4)

list1.addToList(1)
list1.addToList(3)
list1.addToList(4)

list1.printList()


