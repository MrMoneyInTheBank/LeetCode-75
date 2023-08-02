"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


def countSubstrings(s):
    count = 0

    for i in range(len(s)):
        l, r = i, i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1 
            l -= 1 
            r += 1 
        
        l, r = i, i+1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1 
            l -= 1 
            r += 1 
        
    return count
    
# Time | Space : O(n^2) | O(1)

# This solution is basically the same as the longestPalindromicSubstring problem. The difference
# is that we keep a track of all the substrings generated in the count variable instead of the 
# longest one. 

