"""
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node. Both the 
next and random pointer of the new nodes should point to new nodes in the copied list such that 
the pointers in the original list and copied list represent the same list state. None of the pointers 
in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for 
the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented 
as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or 
null if it does not point to any node.

Your code will only be given the head of the original linked list.
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None

    hashmap = {}

    curr = head
    while curr:
        hashmap[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        copy = hashmap[curr]
        copy.next = hashmap[curr.next] if curr.next != None else None
        copy.random = hashmap[curr.random] if curr.random != None else None

    return hashmap[head]

# Time | Space: O(n) | O(n)

# The problem statement is long and confusing but the problem is rather simple. We basically want to
# create an entirely new LinkedList which mimics the given list. We can do this with two passes; the
# first pass takes cares of creating the actual Nodes present. The second pass takes care of assigning
# the correct pointers to each node. In the first pass, we create a new node with the current node's value
# and assign this key (curr) to the value (copy). In the second pass, we get the copy (hashmap[curr]) and
# then get the copy of the next and random nodes and assign them to the current node's copy. In the end
# we return the copy of the head of the list.
