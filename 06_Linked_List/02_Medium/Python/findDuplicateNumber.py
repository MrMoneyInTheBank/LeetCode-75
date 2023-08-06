"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] 
inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

def findDuplicate(nums):
    fast, slow = 0, 0 

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break 

    fast = 0 
    while True:
        fast = nums[fast]
        slow = nums[slow]
        if fast == slow:
            return slow 

# Time | Space: O(n) | O(1)

# This question is basically just an application of Floyd's Tortois and Hare algorithm. We can 
# Think of each number in the array to be a pointer to a node in a linked list. We initialize
# a slow and fast pointer. The slow pointer gets updated to the next node (nums[slow]). The fast
# pointer gets updated the the next to next node (nums[nums[fast]]). If they are at the same node 
# (number), we reset the fast pointer to the head (0) and get the next node for each until they are
# equal. This is the start of the cycle (since it has an indegree of 2). The reason this works is 
# because the fast pointer will at some point jump over the slow pointer. The place that they meet
# will be have the same distance to the cycle start as the head (this can be proven with simple algebraic
# math). 
    