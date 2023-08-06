'''
Given an integer array nums, find the subarray
with the largest sum, and return its sum.
'''

def maxSubArray(nums):
    kadane = [0 for num in nums]
    kadane[0] = nums[0]
    globalMax = nums[0] 

    for i in range(1, len(nums)):
        kadane[i] = max(nums[i], kadane[i-1] + nums[i])
        globalMax = max(globalMax, kadane[i])
    
    return globalMax 

# This is just Kadane's algorithm. Find the maximum sum ending at each index
# Keep track of the maximum overall. 


# Time | Space: O(n) | O(n) 

