""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    """
    Trees: Is This a Binary Search Tree?
    """
    def isbst(root, min_int, max_int):
        if root is None:
            return True
        if root.data >= max_int or root.data <= min_int:
            return False
        return isbst(root.left, min_int, root.data) and isbst(root.right, root.data, max_int)
    import sys
    return isbst(root, -sys.maxsize, sys.maxsize)
