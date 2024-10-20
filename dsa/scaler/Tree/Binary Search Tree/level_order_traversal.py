from collections import deque
from queue import Queue

class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node, data):
        if node is None:
            return Tree(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    
    def level_order(self, root):
        # using deque
        # q = deque()
        # q.append(root)

        # while q.__len__() != 0:
        #     left_data = q.popleft()
        #     print(left_data.data, end='=>')

        #     if left_data.left:
        #         q.append(left_data.left)
        #     if left_data.right:
        #         q.append(left_data.right)

        #using Queue
        Q = Queue()
        Q.put(root)

        while not Q.empty():
            node = Q.get()

            if node is None:
                continue
            print(node.data)
            Q.put(node.left)
            Q.put(node.right)

root = None
object = Tree(root)
root = object.insert(root, 50)
root = object.insert(root, 30)
root = object.insert(root, 20)
root = object.insert(root, 40)
root = object.insert(root, 70)
root = object.insert(root, 60)
root = object.insert(root, 80)
# object.inorder(root)
object.level_order(root)

