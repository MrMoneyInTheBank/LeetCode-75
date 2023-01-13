'''
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all 
the original letters exactly once.
'''

from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        res[key].append(word)
    
    return list(res.values())

# Initialize a dictionary where the keys are the dictinct sorted
# tuple of the words in the array. Iterate through the array. If 
# the sorted tuple if already a key, append the current word to that
# key otherwise create a new key and append the current word to that Key
# By the end of the iteration, the values will be the groups of anagrams.

# Time complexity: O(n^2 log(n))
# Space complexity: O(n)