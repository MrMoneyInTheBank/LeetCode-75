"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


from typing import List 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        currSubset = []

        def backtrack(idx):
            if idx >= len(nums):
                res.append(currSubset.copy())
                return 
        
            currSubset.append(nums[idx])
            backtrack(idx+1)
            currSubset.pop()
            backtrack(idx+1)

        backtrack(0)
        return res 

# Time | Space : O(2^N) | O(N * 2^N)

# When creating a subset of the whole set, we can either add an element to a set and continue
# or choose not to add it to the current subset and continue. This represents the binary choice
# for all elements presents which allows us to generate all subsets of the given set. We declare an
# array res which will hold all the subsets that we have found. We also create an array to store our
# current subset. Next, we define a backtracking function which takes in an index idx and computes
# all the possible subsets that can be created from the current index. The base case for this function 
# is if we reach the end of the array, then we can add the current subset to our answer and return from
# the function. If we have not reached the end, we can first add the current element to our subset and
# continue forming subsets. Now, we pop the current element that we just added and continue forming the
# subsets without adding the current element. In the end, we call this backtracking function and return 
# answer. 