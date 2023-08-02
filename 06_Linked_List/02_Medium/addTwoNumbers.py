"""
ou are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy 
        carry = 0 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 
            
            val = v1 + v2 + carry 
            carry = val // 10 
            val = val % 10 
            cur.next = ListNode(val)
            
            cur = cur.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
            
        return dummy.next
    
# Time | Space : O(max(n, m)) 

# Basically, we add the digits at corresponding places and use that as the value for
# the output list. However, we need to consider if we are carrying any value from the 
# previous addition. This is why we store a carry variable. The carry value is always the
# sum integer divided by 10. The value we place instead is mod 10.
