'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    curr = dummy 

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next 
        else:
            curr.next = list2 
            list2 = list2.next 
        
        curr = curr.next 
    
    if list1:
        curr.next = list1 
    elif list2:
        curr.next = list2 
    
    return dummy.next 

# We create a new linked list two store the sorted elements. At each iteration, we store the smaller element 
# When one list is None, we set the rest of the new list to the remainder of the current list. We then return the
# curr pointer which is the next node of the head of the new list. 

# Time | Space : O(n) | O(n) 

