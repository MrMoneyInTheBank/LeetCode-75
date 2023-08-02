"""
Given an integer array nums, return the length of the longest strictly increasing subsequence
"""

def lengthOfLIS(nums):
    cache = [1 for _ in nums]
    res = 1

    for i in reversed(range(len(nums))):
        for j in range(i+1, len(nums)):
            cache[i] = max(cache[i], 1 + cache[j]) if nums[i] < nums[j] else cache[i]
            res = max(res, cache[i])
        
    return res 

# Time | Space : O(n^2) | O(n)
# If we work backwards, the LIS from index i is adding one to the LIS of the 
# following indices. The maximum of all of the LIS will be the answer

def fasterLengthOfLIS(nums):
    cache = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > cache[-1]:
            cache.append(nums[i])
        else:
            l, r = 0, len(cache) - 1 

            while l <= r:
                mid = (l + r) // 2 

                if cache[i] < nums[i]:
                    l = mid + 1 
                else:
                    r = mid - 1 
            
            cache[l] = nums[i]
        
    return len(cache)

# Time | Space : O(n log(n)) | O(n)

# This solution is much harder to undersand. We maintain a cache of the last element of every subsequence
# of length i. Intially, this cache just has nums[i]. Then we iterate over nums. If nums[i] > cache[-1], then
# we can extend all subsequences found until now and therefore we add this as a tail. Otherwise, we find the lowest
# element in cache greater than nums[i] and replace cache[j] = nums[i]. The reason we do this is that if we 
# find an element greater than the cache[-1], if doesn't matter if we use cache[j] or nums[i] (but we can't use both)
# and to be safe, we should use the larger element. In the end, the cache reprents the elements in the tail of a subsequence
# of length i + 1 and therefore we return the length of the entire cache. 
        