'''
Serialization is the process of converting a data structure 
or object into a sequence of bits so that it can be stored 
in a file or memory buffer, or transmitted across a network 
connection link to be reconstructed later in the same or 
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree 
can be serialized to a string and this string can be deserialized 
to the original tree structure.

Clarification: The input/output format is the same as how LeetCode 
serializes a binary tree. You do not necessarily need to follow this 
format, so please be creative and come up with different approaches 
yourself.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    

class Codec:
    def serialize(self, root):
        res = [] 

        def preOrder(node, arr):
            if not node:
                res.append("N")
                return 
            arr.append(str(node.val))
            preOrder(node.left, arr)
            preOrder(node.right, arr)
        
            return arr 

        preOrder(root, res)

        return res 
    
    def deserialize(self, data):
        vals = data.split(".")
        self.i = 0 

        def dfs():
            if vals[self.i] == "N":
                self.i += 1 
                return None 
            node = TreeNode(vals[self.i])
            self.i += 1 
            node.left = dfs()
            node.right = dfs()

            return node 
        
        return dfs()
    

# If we do a preorder traversal where in we fill in every node including null nodes 
# we can reconstruct a binary tree from it alone. This is the approach used. The 
# preorder traversal if fairly standard with the expection of appending "N" for a null
# node. When we decode, for each root, the first "N" indicates the end of the left subtree
# and the second "N" represents the end of the right subtree. 

# Time | Space: O(n) | O(n) 




