class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertBetween(self, prev_node, data):
        import pdb;pdb.set_trace()
        if prev_node is None:
            print('Previous node should have next node!')
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node
            
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
            
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    
list = LinkedList()
list.append('A')
list.append('B')
list.append('C')
list.prepend('0')
# print(list.head.next.data)
list.insertBetween(list.head.next,'D')
list.print_list()
