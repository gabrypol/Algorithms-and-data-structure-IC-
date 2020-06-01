'''
Write a function to check that a binary tree is a valid binary search tree.

Here's a sample binary tree node class:

  class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
'''

'''
Solution:
In order for a binary tree to be a valid binary search tree, when doing an inorder traversal (left, root, right), the list of items I get should be in ascending order.

Time: O(n)
Space: O(n)
'''


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder_traversal(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def bst_checker(self):
        inorder_list = self.inorder_traversal(self, [])
        for i, num in enumerate(inorder_list[1:], 1):
            if num <= inorder_list[i - 1]:
                return False
        return True

#          4
#       /      \
#      2         6
#    /   \      /  \
#   1     3    5    7


tree = BinaryTreeNode(4)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(6)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(3)
tree.right.left = BinaryTreeNode(5)
tree.right.right = BinaryTreeNode(7)

print("inorder:", tree.inorder_traversal(tree, []))
print("BST check:", tree.bst_checker())
