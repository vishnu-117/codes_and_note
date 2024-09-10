class Node:
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val =  value

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
        
"""
Tree                1
                   / \
                  /   \
                 2      3
                / \
               /   \
              4     5

"""
total_sum = 0
def preorder(root):
    """
    output: 1,2,3,4,5
    """    
    if root:
        total_sum += root.val
        print(root.val)
        preorder(root.left)
        preorder(root.right)
print("==================")
print('pre order traversal>>>>>>>>')
preorder(root)
print("==================")



def inorder(root):
    """
    output: 4,2,5,1,3
    """
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

print("==================")
print('in order traversal')
inorder(root)
print("==================")
        

def postorder(root):
    """
    output: 4,5,2,3,1
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

print("==================")
print('post order traversal')
postorder(root)
print("==================")