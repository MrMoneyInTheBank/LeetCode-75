'''
Given the roots of two binary trees p and q, write a function 
to check if they are the same or not.

Two binary trees are considered the same if they are structurally 
identical, and the nodes have the same value.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sameTree(root1, root2):
    if not root1 and not root2:
        return True 
    if not root1 or not root2:
        return False 
    if root1.val != root2.val:
        return False 
    
    return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

# Similar to the invert Tree function, we visit every node and compare them. 
# We first check if both nodes are None, which is when we return True. 
# If only one node is None, we return False. If the values of the nodes are not 
# equal, we return false as well. Then we explore the left and right subtrees of each tree. 

# Time | Space: O(n) | O(n)