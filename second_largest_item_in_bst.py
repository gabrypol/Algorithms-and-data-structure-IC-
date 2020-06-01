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
Solution 1:
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


'''
Solution 2:
    This solution has both better time and space complexities.

    There are various possible cases in order for one element to be the 2nd largest one in a BST:
        - The parent of the rightmost item (if the parent doesn't have a left child).
        - If the rightmost item doesn't have a right child but a left child, the 2nd largest item in the BST is the largest item of the left subtree.

    Time: O(h) in general. O(logn) if the tree is balanced. O(n) if the tree is a linked list (worst case)
    Space: O(1)



class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root_node):
    if (root_node is None or (root_node.left is None and root_node.right is None)):
        raise ValueError(
            'Tree must have at least 2 nodes, because we are looking for the 2nd largest item.')

    current = root_node
    while current:
        if current.right and not current.right.right and not current.right.left:
            return current.value

        if current.left and not current.right:
            find_largest(current.left)

        current = current.right


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

print(find_largest(tree))
print(find_second_largest(tree))

'''
