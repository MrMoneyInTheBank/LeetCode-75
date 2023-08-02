"""
You are given an array of integers nums, there is a sliding window 
of size k which is moving from the very left of the array to the very 
right. You can only see the k numbers in the window. Each time the 
sliding window moves right by one position.

Return the max sliding window.
"""

import collections
from typing import List 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = r = 0 

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
                l += 1 
            
            if r - l + 1 >= k:
                res.append(nums[q[0]])
            
            r += 1 
        
        return res 

# Time | Space : O(n) | O(n)

# The easy solution to this problem is to track each subsequent window of size k, 
# loop through that window to find the maximum and then append that to the result.
# However, this requires traversing the window while traversing the array so the time
# complexity is O(k * (n-k)). The faster solution uses a deque. The deque holds every element
# in the window but it formed in such a way that the left most element is the greater element
# in the window. When we add elements to the deque, we know that if the element we are adding
# is greater than the elements in the deque, then none of those elements will be considered the 
# maximum element in the window and therefore we can keep popping them off. This way, the only 
# elements that we add to the deque are the maximum elements for each window. Of course, we need 
# to keep track of the window with left and right pointers and pop the front of the queue when we 
# increment the left pointer. 
