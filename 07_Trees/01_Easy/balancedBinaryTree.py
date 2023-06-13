"""
Given a binary tree, determine if it is height-balanced.
"""


def getHeight(node):
    if not node:
        return 0
    left = getHeight(node.left)
    right = getHeight(node.right)

    return 1 + max(left, right)


def isBalanced(root):
    if not root:
        return True 

    left = getHeight(root.left)
    right = getHeight(root.right)

    if abs(left - right) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)

# Time | Space : O(n^2) | O(n)

# Check the height for each subtree and return false if it is not height balanced.


def isBalancedLinear(root):
    def dfs(root):
        if not root:
            return [True, 0]
    
        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1+max(left[1], right[1])]
    
    return dfs(root)[0]