'''
Given the head of a linked list, remove the n'th node
from the end of the list and return the head
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = None 
    

def removeNthFromEnd(head, n):

    dummy = ListNode(0, head)
    left = dummy 
    right = head 

    while n > 0:
        right = right.next 
        n -= 1 
    
    while right:
        left = left.next 
        right = right.next 
    
    left.next = left.next.next 

    return dummy.next


# The approach is to increment one pointer by n so that when the list is traverse from beginning
# One pointer will be at the n'th node when the original pointer points to the end of the list. 
# The reason we are using a dummy node and pointing it to the head of the list is so that when 
# we are done traversing the list, the left node will point to the n'th node and not be the n'th
# node itself 

# Time | Space: O(n) | O(1)