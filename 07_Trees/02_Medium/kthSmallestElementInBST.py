'''
Given the root of a binary search tree, and an integer k, return the k'th 
smallest value (1-indexed) of all the values in the binary search tree. 
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    

def kthSmallest(root, k):
    stack = []
    curr = root 


    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left 
        
        curr = stack.pop()
        k -= 1

        if k == 0:
            return curr.val 
        curr = curr.right 
    
# Alternate solution to show what is going on in the background 

def kthSmallestRecursive(root, k):
    def inOrderTraverse(node, arr):
        if not node:
            return 
        
        inOrderTraverse(node.left, arr)
        arr.append(node.val)
        inOrderTraverse(node.right, arr)

        return arr 
    
    inOrder = inOrderTraverse(root, [])

    return inOrder[k-1]

# If we can sort the nodes in order, then we just need to return the k-1 index node. 
# We can do this easily by doing a recursive in order traversal but that uses extra memory
# and if k is small then we will be traversing more nodes than necessary. The way a in order 
# traveral works is we visit the node, store it to come back to that node later on, explore the 
# left subtree until it is empty, come back to the previous node, take account of its value, and 
# then we visit the right subtree. The optimal solution is an iteration implementation of the in order
# traversal. The stack keeps a track of which node we need to come back to. Initially it is empty. After
# the first node, we add the root to the stack. Then we need exploring the left subtree until it is empty 
# while appending the previous node to the stack. Once the left subtree is empty, we come back to the previous
# node by stack.pop(). If we have reached the desired level, then we can return the value. Otherwise, since we have
# already traversed the left subtree of the node and the node itself, we set the current node to the right child 
# or the previous node. 


# Time | Space: O(n) | O(n) 
    