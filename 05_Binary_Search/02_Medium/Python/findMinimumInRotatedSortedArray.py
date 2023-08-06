'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''


def findMin(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (r + l) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    return nums[l]

# We do a binary search until we find the pivot point where all nums to the left are greater
# and all nums to the right are larger. Since this is a sorted rotated array, the number at 
# the pivot point will be the minimum 

# Time | Space: O(log(n)) | O(1)