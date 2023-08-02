"""
Given a string s, return the longest palindromic substring in s.
"""

def longestPalindromicSubstring(string):
    res = ""
    mx = 0 

    for i in range(len(string)):
        l, r = i, i

        while l >= 0 and r < len(string) and string[l] == string[r]:
            if (r - l + 1) > mx:
                mx = r - l + 1
                res = string[l: r+1]
            l -= 1 
            r += 1 

        l, r = i, i + 1

        while l >= 0 and r < len(string) and string[l] == string[r]:
            if (r - l + 1) > mx:
                mx = r - l + 1
                res = string[l: r+1]

            l -= 1 
            r += 1
        
    return res

# Time | Space: O(n^2) | O(1)

# For each index in the array, consider it as the middle position of a palindromin substring 
# and expand outwards. To consider odd strings, we need the current element to be the center
# therefore we check immediately left and right. To consider even strings, we need the current
# letter and the next letter to act as the 'center' so we consider l = i and r = i+1 


            
        