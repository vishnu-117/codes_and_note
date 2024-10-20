# Python3 program to find the maximum depth of tree

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

class Solution:
    def searchBST(self, root, val):
        result = []
        if root == None:
            print('not found>>>>>>>>>>')
            return None
        if root.val == val:
            print(root.val,'found>>>>>>>>>>>>>>>')
            # result.append(root.val)
            self.searchBST(root.left, val)
            self.searchBST(root.right, val)
            return
        if val > root.val:
            self.searchBST(root.right, val)
        if val < root.val:
            self.searchBST(root.left, val)

solution = Solution()
print(solution.searchBST(root, 2))