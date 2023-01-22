'''
You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night. 

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police. 
'''

def rob(nums):
	rob1, rob2 = 0, 0 

	for money in nums:
		temp = max(rob1 + money, rob2)
		rob1 = rob2 
		rob2 = temp 
	
	return rob2 


# We will use dynammic programming to solve this question. rob1 indicates the maximum amount of money
# that can be robbed until (and including) the previous house, rob1 indicates the maximum amount of money that can be 
# robbed until (and including) the current house. At each iteration in the loop, we calculate the maximum we can 
# loot from the current house, can then since moving forward, the current house will become the previous house for
# the next house, we update r1 and set it to r2, and we set r2 to the value we just calculated. 
 
# Time | Space: O(n) | O(1) 
