class Node:
    
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse_ll_recursion(self, head):
        if head is None or head.next is None:
            return head
        
        reversed_head = self.reverse_ll_recursion(head.next)
        head.next.next = head
        head.next = None
        return reversed_head
    
    def reverse_ll_iterative(self, head):
        prev = None
        current = head

        # Traverse the list
        while current:
            # Store the next node
            next_node = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move prev and current pointers one step forward
            prev = current
            current = next_node
        # tmp = None
        # tmp_head = head
        # while head != None:
        #     tmp2 = head.next
        #     head.next = tmp
        #     tmp = head
        #     head = tmp2
        return prev

    def pp_linked_list(self, head):
        tmp = head
        while tmp:
            print(tmp.item, end="->")
            tmp = tmp.next
        print()

if __name__ == '__main__':
    linked_list = LinkedList()

    head = Node(1)
    linked_list.head = head
    second = Node(2)
    third = Node(3)

    linked_list.head.next = second
    second.next = third

    linked_list.pp_linked_list(head)
    head = linked_list.reverse_ll_iterative(head)
    linked_list.pp_linked_list(head)
    # head = linked_list.reverse_ll_recursion(head)
    # linked_list.pp_linked_list(head)






