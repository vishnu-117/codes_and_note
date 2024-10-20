class Node:
    
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def print_ll(self):
        node = self.head
        while node is not None:
            print(node.item)
            node = node.next

    def remove_from_last(self):
        node = self.head

        if node.next is None:
            self.head = None
        elif node.next.next is not None:
            node = node.next
        tmp = node.next
        node.next = None
        tmp = None
    
    def remove_node(self, data):
        node = self.head

        if node.item == data and node.next is not None:
            self.head = self.head.next
        
        while node.next is not None:
            if node.next.item == data:
                tmp = node.next
                node.next = node.next.next
                tmp.next = None
                tmp = None
                break
            node = node.next


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node('vtu')
    third = Node(3)

    linked_list.head.next = second
    second.next = third

    linked_list.remove_node(1)
    linked_list.print_ll()




        

