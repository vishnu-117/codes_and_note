class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def insert_start(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_end(self, value):
        new_node = Node(value)

        tmp = self.head

        while tmp.next is not None:
            tmp = tmp.next
        
        tmp.next = new_node
    
    def insert_at_nth(self, value, n):
        temp = self.head
        new_node = Node(value)

        for i in range(n-1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node        

    def remove(self, value):
        if self.head is None:
            return

        temp = self.head
        previous_node = None

        while temp is not None and temp.data != value:
            previous_node = temp
            temp = temp.next
        
        if temp is None:
            return
        
        if previous_node is None:
            self.head = temp.next
        else:
            previous_node.next = temp.next

#print LL

ll = LinkedList()

ll.insert_start(60)
ll.insert_start(50)
ll.insert_start(40)
ll.insert_start(30)
ll.insert_end(80)
ll.insert_end(90)
ll.insert_at_nth(11, 2)
# ll.remove(90)
# instance1 = Node(10)
# instance2 = Node(20)
# instance3 = Node(30)

# ll.head = instance1
# ll.head.next = instance2
# instance2.next = instance3

tmp = ll.head
while tmp:
    print(tmp.data, '-->',end=" ")
    tmp = tmp.next
