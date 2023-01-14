'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList(head):
    curr, prev = head, None 

    while curr:
        nxt = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nxt 
    
    return prev 


# At each iteration, we take the current node, store the next node, and redirect the next pointer
# to the previous node which will be initially None. we then update the prev, and curr nodes. At
# the end, the curr node will be None and the prev node will be at the end of the list which is the
# new head so we return prev 

# Time | Space: O(n) | O(1) 
