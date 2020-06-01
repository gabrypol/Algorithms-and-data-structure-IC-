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

#          4
#       /      \
#      2         6
#    /   \      /  \
#   1     3    5    7


myTree = BinaryTreeNode(4)
myTree.left = BinaryTreeNode(2)
myTree.right = BinaryTreeNode(6)
myTree.left.left = BinaryTreeNode(1)
myTree.left.right = BinaryTreeNode(3)
myTree.right.left = BinaryTreeNode(5)
myTree.right.right = BinaryTreeNode(7)


def bst_checker(my_list):
    for i, num in enumerate(my_list[1:], 1):
        if num <= my_list[i - 1]:
            return False
    return True


print("inorder:", myTree.inorder_traversal(myTree, []))
print(bst_checker(myTree.inorder_traversal(myTree, [])))
