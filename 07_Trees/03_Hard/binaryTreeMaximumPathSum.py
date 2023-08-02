'''
A path in a binary tree is a sequence of nodes where each pair of adjacent 
nodes in the sequence has an edge connecting them. A node can only appear 
in the sequence at most once. Note that the path does not need to pass through 
the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val 
        self.left = left 
        self.right = right 
    

def maxPathSum(root):
    res = [root.val]

    def dfs(node):
        if not node:
            return 0

        left, right = dfs(node.left), dfs(node.right)
        left, right = max(left, 0), max(right, 0)

        res[0] = max(res[0], node.val + left + right)

        return node.val + max(left, right)

    dfs(root)
    return res[0]

# Notice that there can be only one split in a path since if there are two then
# the path is no longer continuous and there must be a reversal within it. For 
# each node, the max path sum will be the left path sum, the right path sum, or
# we can join the paths by adding the nodes value but keep in mind that when we 
# are using this node's information for the nodes above, we cannot return the  
# joint path since we have already had a split, which is why we will return 
# node.val + max(left, right) however, we will keep a track of the global variable
# even with a split. We don't care what the dfs function returns because the the 
# overall tree, either we take the max path sum from the left subtree, the right 
# subtree, or we join the two paths. res[0] will already be the maximum of the left
# subtree and right subtree, and the last check we are doing is by adding the current 
# node's value.

# Time | Space: O(n) | O(n)
