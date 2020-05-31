'''
Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

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
I want to implement an iterative approach, using a depth-first walk approach. Depth-first, as opposed to breadth search, gives us the chance of short-circuiting: we could find two depths more than 1 level apart at the beginning of our walk; if that happens, we return False (meaning that the tree is not "Superbalanced") without having to traverse the whole tree.

I create a 'depth' list containing all the depths of the leaves found so far. We can return False if 'depth' contains more than two elements or if it contains exactly two elements whose difference is greater than 1.

Time: O(n)
Space: O(d) where d is the depth of the tree. "depths" can at most contain three elements --> O(1). "nodes" can at most contain d elements.
'''


def is_superbalanced(root):
    if root == None:
        return True
    depths = []
    nodes = []
    nodes.append((root, 0))
    while len(nodes):
        node, depth = nodes.pop()
        if not node.left and not node.right:
            if depth not in depths:
                depths.append(depth)
            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                return False
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
    return True
