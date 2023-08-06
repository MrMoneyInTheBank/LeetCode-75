"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes 
is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional[Node] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseNodesInGroup(self, head: Optional[Node], k: int) -> Optional[Node]:
        dummy = Node(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKthNoth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = curr.next

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKthNode(self, head: Optional[Node], k: int) -> Optional[Node]:
        curr = head

        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr


# Time | Space : O(n) | O(1)

# since we are going to be modifying the head, its good to have a dummy node which points to the head
# so that we can return the linked list using dummy.next at any time. The basic idea behind this problem
# is an extension on just reversing a linked list. Each group will have the start of the group, the end
# of the previous group, the end of the current group, and the start of the next group. First, we count
# K nodes from the end of the previous group. If this is the null node then we break out of this reversing
# loop. Next, we store the start of the next group in groupNext = kth.next. Now, we reverse this group.
# After reversing this group, remember that groupPrev.next points to the former starting node. We save this
# information since this node is now the end of this current group and the break this link and assign
# groupPrev.next to the start of this group which is the Kth node.
