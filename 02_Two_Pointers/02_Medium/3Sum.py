'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

def threeSum(nums):
    res = [] # Initialize return array 
    nums.sort() # Sort the input array to optimize time 

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]: # if current starting value has been seen
            continue 

        l, r = i + 1, len(nums) - 1 # searching for the other two values which sum to -a
        while l < r:
            b, c = nums[l], nums[r]
            total = a + b + c
            if total > 0: # if too large, decrement the bigger value
                r -= 1
            elif total < 0: # if too big, increment the smaller value
                l += 1
            else:
                res.append([a, b, c,]) # appent triplet
                l += 1 # increment smaller counter
                while nums[l] == nums[l-1] and l < r: # make sure second number hasn't been seen already 
                    l += 1 
                
                # don't need to alter right pointer since the aforementioned conditions will adjust for it
                # each unique second summand will have a corresponding third summand
    return res 

# Time | Space: O(n) | O(n)