'''
Given an integer array nums and an integer k, 
return the k most frequent elements. You may 
return the answer in any order.
'''

from collections import defaultdict

def topKFrequent(nums, k):
    freq = defaultdict(int)

    for num in nums:
        freq[num] += 1
    
    pairs = [[key, value] for key, value in freq.items()]
    pairs.sort(key=lambda x: x[1], reverse=True)
    res = []

    for i in range(k):
        res.append(pairs[i][0])
    
    return res 

# Create a dictionary which holds the frequencies of all 
# the numbers in the array. Sort the dictionary in descending
# order. Return the first k numbers in the sorted dictionary

# Time Complexity: O(n^2 log(n))
# Space Complexity: O(n)

