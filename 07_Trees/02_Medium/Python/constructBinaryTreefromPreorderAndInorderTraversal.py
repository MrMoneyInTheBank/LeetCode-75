'''
Given two integer arrays preorder and inorder where preorder is the
preorder traversal of a binary tree and inorder is the inorder traversal
of the same tree, construct and return the binary tree 
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None 
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid+1], inorder[mid+1:])

    return root 

# The first element in the preorder traversal is the root of the tree. For a node 
# in the inorder traversal, all nodes to the left are in the left subtree of the node
# and all nodes to the right are in the right subtree of the node. In the solution, we
# first check if either array is empty because if it is then the node is None since we 
# dont have any information for it which is only true of null nodes. After this, we take 
# the first element of the preorder traversal and make it the root. We then find the index of 
# the root in the inorder traversal to find the number of nodes in the left subtree and the right 
# subtree. We call the function again to find the left subtree but only pass it the preorder nodes 
# which are in the left subtree, we do this by creating a subarray for the preorder traversal and only 
# passing in the number of nodes to the left of the root in the inorder traversal. Analogously, we modify
# the inorder traversal to only contain nodes to the left of the root. We do the same process for the right subtree. 
# We can then return the root 

# Space | Time: O(n) | O(n) 
