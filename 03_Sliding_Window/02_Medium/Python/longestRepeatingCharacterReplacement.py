'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''

def lengthOfLongestSubstring(string):
    charSet = set()
    l = 0 
    res = 0 

    for r in range(len(string)):
        while string[r] in charSet:
            charSet.remove(string[l])
            l += 1
        charSet.add(string[r])
        res = max(res, r - l + 1)
    
    return res


# Each letter can be a starting letter of a substring. From the first character, 
# keep increasing the right pointer until a duplicate is not found. This can be checked
# by adding the letters of the substring in a set. If a duplicate is found, shrink the window
# by incrementing the left pointer until there are no duplicates. We also need to keep removing 
# the corresponding characters from the set. 

# Time | Space: O(n) | O(n)
