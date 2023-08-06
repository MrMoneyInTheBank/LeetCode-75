"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 

def rightSideView(root):

    res = collections.defaultdict(int)

    q = collections.deque([(root, 0)])

    while q:
        node, lvl = q.popleft()
        if not node:
            continue
        res[lvl] = node.val
        q.append((node.left, lvl+1))
        q.append((node.right, lvl+1))

    return list(res.values())

# Time | Space : O(V + E) | O(h)

# Do a bfs and keep track of the last node on each level. Return the nodes as a list 
