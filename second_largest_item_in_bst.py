'''
Write a function to find the 2nd largest element in a binary search tree.

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
Doing an inorder traversal of valid binary search tree, I get a list of ascending elements.
Therefore, the 2nd largest element in the bst is the 2nd to last element of the list I get from the inorder traversal.

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

    def find_2nd_largest_item(self):
        inorder_list = self.inorder_traversal(self, [])
        return inorder_list[-2]


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

print("inorder traversal:", tree.inorder_traversal(tree, []))
print("2nd largest item:", tree.find_2nd_largest_item())
