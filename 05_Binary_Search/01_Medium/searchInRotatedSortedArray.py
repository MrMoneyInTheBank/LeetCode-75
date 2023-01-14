'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

def search(nums, target):
    left, right = 0, len(nums) - 1 

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid 
        elif nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1 
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1 
            else:
                right = mid - 1 

    return - 1

# we do a binary search for this problem. At each iteration, we find the middle of the current
# subarray. If the element at the middle is the target then we can return middle. Else, if the 
# target element is within the left subarray, which we can check in constant time, we make the right
# pointer mid - 1. Analogous adjustment for the right subarray. 

# Time | Space: O(log (n)) | O(1) 
