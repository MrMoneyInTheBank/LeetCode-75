"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""

def maxProduct(nums):
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:

        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

# Time | Space : O(n) | O(1)

# If the array was only positive integers, then we can return the product of the array. 
# when there are negative integers, the current maximum until this point will be the largest 
# negative number since it is multiplied by -1. For the same reason, the current minimum until
# this point will be the largest number since it will be least affected by the mirroring. Since
# we want to know the largest product of the contiguous subarray, we can do something similar to 
# kadane's algorithm. We maintain the currentMax, currentMin, and a global maximum res. Initially, 
# they are all set to 1. For each num in nums, we calculate the currentMax, currentMin, and recompute
# res. We return res at the end. 
