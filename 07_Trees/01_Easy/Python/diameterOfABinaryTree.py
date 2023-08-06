'''Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes 
in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right
    
class Info:
    def __init__(self, diam, height):
        self.diam = diam 
        self.height = height

def helper(root):
    if not root:
        return Info(-1, 0)

    left = helper(root.left)
    right = helper(root.right)

    leftDiam, leftHeight = left.diam, left.height
    rightDiam, rightHeight = right.diam, right.height

    diam = max(leftDiam, rightDiam, leftHeight + rightHeight)
    height = 1 + max(leftHeight, rightHeight)

    return Info(diam, height)

def diameterOfBinaryTree(root):
    return helper(root).diam

# Time | Space : O(n) | O(n)

# For each node, the diameter of the subtree rooted at that node is maximum of the left subtree 
# diameter, the right subtree diameter, or we can join the heights of the left and right subtrees
# by creating a path through the root node. We can store this info in a class and recurse on the
# whole tree and return the diameter in the end. 

# we could also solve this using a dfs without any classes with a similar spacetime complexity

def diamterOfBinaryTreeAlternate(root):
    res = 0 

    def dfs(node):
        nonlocal res

        if not node:
            return 0 # leaf nodes have height 0 
    
        left = dfs(node.left) # get height of left subtree
        right = dfs(node.right) # get height of right subtree

        res = max(res, left + right) # diameter of the tree is the max between the current diameter found and the sum of left height and right height

        return 1 + max(left, right) # return the height of the current subtree

    dfs(root)
    return res