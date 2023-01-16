'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST)

A valid BST is defined as follows: 
    - The left subtree of a node contains only nodes with keys less than the node's key. 
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False

        return valid(node.left, left, node.val) and valid(
            node.right, node.val, right
        )

    return valid(root, float("-inf"), float("inf"))

# Each node must be between the minimum value and the maximum value seen so far. For the 
# root, the minimum is -infinity and the maximum is infinity. For every subsequent node, 
# the minimum value increases and the maximum value decreases. This is why we have a helper 
# function doing most of the work. 


# Time | Space: O(n) | O(n) 