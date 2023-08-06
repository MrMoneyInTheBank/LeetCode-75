'''
Given the root of a binary tree, invert the tree, and return its root
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    
def invertTree(root):

    if not root:
        return None 
    
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)
    return root 


# The idea is simple. If the tree is empty, return None. Otherwise, swap the children and call 
# the function on the children. At the end, return the root 

# Time | Space: O(n) | O(h) 

# Linear time since we need to visit all nodes and not just all branches 
# Linear space because of the recursion call stack 
