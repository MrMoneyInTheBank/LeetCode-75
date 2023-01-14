'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def hasCycle(head):
    seen = set()

    curr = head 

    while curr:
        if curr not in seen:
            seen.add(curr)
        else:
            return True
    
    return False 

def hasCycleConstantSpace(head):
    slow, fast = head, head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast:
            return True 
        
    return False 


# In the naive, solution we costs extra space, we simply traverse the list and keep a store of 
# the nodes which we have already seen. We return True if any node is present in the set. If we
# traverse the whole list, then we can return False. In the solution with constant space, we keep 
# track of two pointers slow and fast where fast moves at twice the speed of slow. If there is no
# cycle in the list, then the fast pointer will reach the end of the list before the slow pointer. 
# If there is a cycle in the list then the fast pointer will never reach the end of the list and 
# eventually the slow pointer will catch up to it. 

# Time | Space : O(n) | O(1)/O(n) 
