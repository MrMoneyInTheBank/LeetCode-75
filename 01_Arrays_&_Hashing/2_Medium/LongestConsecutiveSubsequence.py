'''
Given an unsorted array of integers nums, 
return the length of the longest consecutive 
elements sequence.
'''

def longestConsecutive(nums):
    unique = set(nums)
    longest = 0 

    for num in nums:
        if num - 1 not in unique:
            l = 0
            while n + l in unique:
                l += 1
            
            longest = max(longest, l)
        
    
    return longest 

# The start of a subsequence will be such a number such that 
# num - 1 is not in the array. We store the unique numbers in a 
# set for constant time lookup. Once we get to such a number by 
# traversing the array, we loop until l such that num + l is not
# in the array. This is the length of this consecutive subsequence. 
# We keep track of the maximum length. 

# Time | Space: O(n) | O(n)