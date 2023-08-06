'''
Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).
'''
import collections 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    
def levelOrder(root):
    res, maxLevel = [], 0
    queue = collections.deque([{"node": root, "lvl": 0}])

    while queue:
        currData = queue.popleft()
        currNode = currData["node"]

        if not currNode:
            continue 
        
        currLevel = currData["lvl"]
        if currLevel >= maxLevel:
            res.append([currNode.val])
            maxLevel = currLevel + 1
        else:
            res[currLevel].append(currNode.val)
        
        queue.append({"node": currNode.left, "lvl": currLevel + 1})
        queue.append({"node": currNode.right, "lvl": currLevel + 1})
    
    return res 


# This solution uses a breadth-first search implemented with a queue to traverse the nodes 
# level by level. We also keep track of the levels that we have already seen and append to 
# the appropriate sublist or create a new sublist if needed. 

# Time | Space: O(n) | O(n) 
