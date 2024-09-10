class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, node, data):
        if node is None:
            return Node(data)

        if  data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def search(self, root, data):
        if root is None:
            print('Not found')
        elif data == root.data:
            print('Element Found')
        elif data < root.data:
            self.search(root.left, data)
        elif data > root.data:
            self.search(root.right, data)

    def findMinFromRightSubTree(self, node):
        tmp = node

        while tmp.left is not None:
            tmp = tmp.left

        return tmp

    def delete_node(self, root, data):
        if root is None:
            return root
        
        if data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp
            
            temp = self.findMinFromRightSubTree(root.right)

            root.data = temp.data

            root.right = self.delete_node(root.right, temp.data)
        return root

root = None

object = Node(root)

root = object.insert(root, 8)
root = object.insert(root, 3)
root = object.insert(root, 1)
root = object.insert(root, 6)
root = object.insert(root, 7)
root = object.insert(root, 10)
root = object.insert(root, 14)
root = object.insert(root, 4)

# object.search(root, 11)
object.delete_node(root, 8)
object.inorder(root)


