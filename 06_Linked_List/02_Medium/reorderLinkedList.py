



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
    

def reorderList(head):
    slow, fast = head, head 

    while fast and fast.next:
        slow = slow.next  
        fast = fast.next 
    
    head2 = slow.next 
    slow.next = None 

    prev, curr = None, head2 

    while curr: 
        nxt = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nxt 
    

    first, second = head, prev 

    while second:
        nxt1, nxt2 = first.next, second.next 
        first.next = second 
        second.next = nxt1 
        first = nxt1
        second = nxt2 
    
    # Function does not return anything but we could using 
    # return head 

# The approach is two divide the list into two, reverse the second half of the list
# alternate between picking elements from the first half and the second half until
# all elements have been added to the list 

# Note that when using the fast and slow pointers to find a cycle in a linked list or 
# using it to find the middle of a linked list, when slow = fast = head, and fast = fast.next.next 
# and slow = slow.next, at the end of the loop, the slow pointer will be at the middle element in the
# list. But when slow = head, fast = head.next, the slow pointer will eventually point towards the middle
# element of the list 


# Time | Space: O(n) | O(n) 

