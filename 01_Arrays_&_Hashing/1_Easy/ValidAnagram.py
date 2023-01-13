'''
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, typically 
using all the original letters exactly once.
'''

def isAnagram(s, t):
    return True if sorted(s) == sorted(t) else False 

# If two strings are anagrams, then if we sorted the letters
# of both strings, they should both be equal to each other. 

# Time Complexity: O(n log(n))
# Space Complexity: O(n) since we are not sorting the strings 
#                   and storing a list of the sorted letters