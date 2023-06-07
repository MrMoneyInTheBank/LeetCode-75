'''
Given the roots of two binary trees root and subroot, return 
true if there is a subroot of root with the same structure and 
node values of subroot and false otherwise

A subtree of a binary tree tree is a tree that consists of a node 
in tree and all of this node's descendants. The tree could also be 
considered as a subtree of itself
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    

def isSubtree(root, subRoot):
    if not root and not subRoot:
        return True 
    if not root:
        return False 
    
    if sameTree(root, subRoot):
        return True 
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False

    return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)


# Very similar to the last problem, just check each node if the subRoot is the same tree 
# as the tree that starts on the current node 

# Time | Space: O(n^2) | O(n)