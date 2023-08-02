"""Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

from typing import List 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        currentSum = sum(nums)
        supposedSum = (n * (n+1)) // 2

        return supposedSum - currentSum

# Time | Space : O(n) | O(1)

# The missing number will acount for the different between the current sum and the supposed sum.
