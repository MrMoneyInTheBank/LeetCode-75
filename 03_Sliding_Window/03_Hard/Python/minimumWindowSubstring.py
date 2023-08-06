'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''

from collections import defaultdict


def inside(chars, window):
    for key, value in chars.items():
        if key not in window or window[key] == 0:
            return False
        elif window[key] < value:
            return False

    return True


def minWindow(s, t):
    tCount = defaultdict(int)
    for char in t:
        tCount[char] += 1

    windowCount = defaultdict(int)
    res = ""
    l = 0

    for r in range(len(s)):
        windowCount[s[r]] += 1

        while inside(tCount, windowCount):
            windowCount[s[l]] -= 1
            l += 1

            #res = s[l-1:r+1]
            if res == "" or len(res) > len(s[l-1:r+1]):
                res = s[l-1:r+1]

    return res

# First, store a frequency count of all the characters in t. This will be used in the helper 
# function which checks if one dictionary is a subset of another. Next, create a window. Increase
# the right index until the window is valid, at which point, increase the left window until the window 
# is no longer valid. This will allow us to get all valid windows. Keep the shorted valid window. 

# Time | Space : O(n) | O(n)