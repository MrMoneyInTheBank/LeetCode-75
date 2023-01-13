'''
Given an array of numbers, return True if there is a duplicate
number else return False
'''


def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True 
        seen.add(nums)
    
    return False 


# As we are traversing the array, we keep track of
# the numbers that we have seen already. If at any point
# we come across a number that we have already seen, then
# we can return True. If we traverse the whole array without
# finding a number that we have already seen then we can return 
# False 

# We can also implement the solution as 

def alternate(nums):
    return True if len(nums) > len(set(nums)) else False
