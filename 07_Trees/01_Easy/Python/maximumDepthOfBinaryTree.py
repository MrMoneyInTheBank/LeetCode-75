'''
Given the root of a binary tree, return its maximum depth

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the furthest 
leaf node
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if root is None:
        return 0 
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    

# This is using a depth-first search on the nodes to find the longest path 
# If the node is None, this can only be achieved if the previous node of a leaf
# node or if the previous node only had one child. Eventually, all leaf nodes will 
# get the value 1 which will represent the number of nodes in the deepest path passing
# through that node. In the end, we add the root node to the count of the longest path 

# Time | Space: O(n) | O(h)