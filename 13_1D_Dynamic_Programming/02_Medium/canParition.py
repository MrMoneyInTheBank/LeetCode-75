"""
Given an integer array nums, return true if you can partition the array into 
two subsets such that the sum of the elements in both subsets is equal or false 
otherwise.
"""

def canParition(nums):
    if sum(nums) % 2 == 1:
        return False 
    
    seen = set([0])

    for i in reversed(range(len(nums))):
        curr = set()
        for _sum in seen:
            if _sum + nums[i] == sum(nums) // 2:
                return True 
            curr.add(_sum)
            curr.add(_sum + nums[i])
        seen = curr 
    return False 

# Time | Space : O(n^2) | O(n)

# If the sum of the array is odd, we return False since we can't half it. 
# Working backwards, we build out all of the possible sums. If we ever, 
# find the target, we return True. If the loop ends without finding the 
# target, we return False. 
