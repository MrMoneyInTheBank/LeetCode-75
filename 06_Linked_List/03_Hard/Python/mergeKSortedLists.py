'''
You are given an array of k linked-lists lists, each 
linked-list is sorted in ascending order. 

Merge all linked-lists into one sorted linked-list and return it
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
    
def mergeKLists(lists):
    if not lists or len(lists) == []:
        return None 
    
    while len(lists) > 1:
        merged = [] 

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None 
        
            merged.append(mergeList(l1, l2))
        
        lists = merged 
    
    return lists[0] 

def mergeList(l1, l2):
    dummy = ListNode()
    curr = dummy 

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1 
            l1 = l1.next 
        else:
            curr.next = l2 
            l2 = l2.next 
        curr = curr.next 
    
    return dummy.next 


# The idea is to pick pairs of linked lists from the array and merge them with a funciton 
# that we have already written to merge two sorted linked lists. If there are an odd number 
# of lists then we merge the last list with an empty lists. We keep doing this until we have 
# only one list 

# Time | Space: O(n log(k)) | O(n)

# O(n) because we have to traverse each list during an iteration
# O(log(k)) because we have to pair up at most k lists. 

