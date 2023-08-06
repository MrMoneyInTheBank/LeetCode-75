"""
Given an array of integers nums which is sorted in ascending order, and 
an integer target, write a function to search target in nums. If target 
exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

def main(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m 
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    
    return -1 

# T | S = O(log(n)) | O(1)