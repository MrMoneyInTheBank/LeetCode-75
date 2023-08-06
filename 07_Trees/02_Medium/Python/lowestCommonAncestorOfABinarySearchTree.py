'''
Given a binary search tree(BST), find the lowest common 
ancestor(LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest 
common ancestor is defined between two nodes p and q as the 
lowest node in T that has both p and q as descendants(where 
we allow a node to be a descendant of itself).”
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    

def lowestCommonAncestor(root, p, q):
    
    curr = root 

    while root:
        if p.val > curr.val and q.val > root.val:
            curr = curr.right 
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left 
        else:
            return curr 
        

# If both p and q are smaller, then we need to check in the left subtree. If both are greater, 
# then we need to check in the right subtree. However, if neither of these conditions are met, 
# this means that p and q are in different subtrees of the current node which is why we can return
# that node 


# Time | Space: O(log(n)) | O(1) 
