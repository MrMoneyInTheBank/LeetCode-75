"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant 
extra space.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res

# Time | Space : O(n) | O(1)
# We need to make use of the XOR operation. The XOR operation takes two inputs, if the input
# bits are the same, then the output will be 0, otherwise, the output will be 1. If we set one,
# of the inputs to be 0 in the beginning, when we take the XOR with another input (not zero), the
# output will be that other input. We can use this throughout the loop. Initialize res to 0. For
# each num in nums, take the XOR with that num. Since each num but one appears twice, this will essentially
# cancel out the effects of the duplicates leaving us with 0^x where x is the unique integer.
