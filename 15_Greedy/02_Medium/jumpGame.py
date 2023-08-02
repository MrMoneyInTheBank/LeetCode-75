'''
You are given an integer array nums. You are initially positioned 
at the array's first index, and each element in the array represents 
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''



def canJump(nums):
    currMax = 0

    for i, n in enumerate(nums):
        if i > currMax:
            return False
        currMax = max(currMax, i + n)

    return True


# Initialize a variable which holds the the furthest index that we can reach 
# as we loop through the elements in nums. Initially, this will be set to 0. 
# At each iteration, if the current index is greater than the maximum index 
# that we can reach then return false since we know that this is an index 
# that we cannot reach using any of the elements prior. Update the furthest 
# reachable index to be the maximum of what it already is and the index we 
# can reach given the current index we are at and the jump we can make from 
# there. If the loop ends, then we can return True since there was never any 
# index that we could not reach.

# Time | Space: O(n) | O(1) 
