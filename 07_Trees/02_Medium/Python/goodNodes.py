"""
Given a binary tree root, a node X in the tree is named good if in the path from 
root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""



def goodNodes(root):
    count = 0
    def dfs(node, currMax):
        nonlocal count
        if not node:
            return 
        
        if node.val >= currMax:
            count += 1
        
        dfs(node.left, max(currMax, node.val))
        dfs(node.right, max(currMax, node.val))

    
    dfs(root, float("-inf"))
    return count

# Time | Space : O(V+E) | O(E)

# Traverse all paths with dfs and keep track of the maximum element in the path so far for comparison
# increment the counter for good nodes. 