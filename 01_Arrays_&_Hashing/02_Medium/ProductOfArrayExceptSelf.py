'''
Given an array of integers, return a new array such that each element
at index i of the new array it the product of all the numbers in the 
original array expect the number at index i
'''


def productExceptSelf(nums):
    '''
    Given an integer array nums, returns an array res
    where res[i] is the product of all the numbers in nums
    except the number at index i
    '''

    # Get an array of the running left subarray products
    pref_prod = []

    for i in range(len(nums)):
        if i == 0:
            pref_prod.append(nums[0])
        else:
            pref_prod.append(nums[i] * pref_prod[-1])

    # Get an array of the running right subarray products
    suff_prod = [0 for num in nums]

    for i in reversed(range(len(nums))):
        if i == len(nums) - 1:
            suff_prod[i] = nums[-1]
        else:
            suff_prod[i] = nums[i] * suff_prod[i+1]

    # Initialize a results array
    res = [0 for num in nums]

    # Each index i will have the value be the product of
    # The last i + 1 numbers times the first i - 1 numbers
    # Obvious exception for the start and end
    for i in range(len(res)):
        if i == 0:
            res[i] = suff_prod[1]
        elif i == len(res) - 1:
            res[i] = pref_prod[-2]
        else:
            res[i] = pref_prod[i-1] * suff_prod[i+1]

    return res

    # Space-time complexity: O(n) | O(n)
    # Linear time since we are only iterating over the input array
    # Linear space since we have to store the prefix, suffix and res products
    ## each of which are the same size as the input
