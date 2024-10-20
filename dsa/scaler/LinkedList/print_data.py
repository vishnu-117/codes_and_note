class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

linkedlist = LinkedList()

head = Node(10)
second = Node(20)
third = Node(30)

linkedlist.head = head
linkedlist.head.next = second
second.next = third

temp = linkedlist.head
while temp:
    print(temp.data)
    temp = temp.next



        
    