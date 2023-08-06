'''
You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed. All houses at this place are arranged in a circle. That means the 
first house is the neighbour of the last one. Meanwhile, adjacent houses have a security system
connected, and it will automatically contact the police if two adjacent houses were broken into 
on the same night. 

Given an integer array nums, representing the amount of money in each house, return the 
maximum amount of money you can rob tongiht without alerting the police. 
'''


def rob(nums):
	
	def helper(arr):
		r1, r2 = 0, 0 

		for n in arr:
			tmp = max(r1 + n, r2)
			r1 = r2 
			r2 = tmp 

		return r2 

	if len(nums) <= 2:
		return max(nums)
		
	return max(helper(nums[:-1]), helper(nums[1:]))

# Note that if the first house is robbed, then the last house cannot be robbed and vice versa
# Therefore we can treat this circular array as two subarrays where in we discount the first 
# house in one of them and discount the last house in the other one. We return return the maximum
# that we can rob from these two arrays. We can use the original function from house robber to make 
# our life easier. 

# Time | Space: O(n) | O(1) 
