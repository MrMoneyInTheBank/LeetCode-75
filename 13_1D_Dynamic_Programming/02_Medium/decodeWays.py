"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using 
the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped 
into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is 
different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

def decodeWays(s):
    dp = {len(s) : 1}

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
        
        if i + 2 <= len(s) and (s[i+1] == '1' or (s[i+1] == '2' and s[i+2] in '0123456')):
            dp[i] += dp[i+2]
        
    return dp[0] 

# Time | Space : O(n) | O(n)

# Working backwards, we can consider the current index as a single integer or couple it with the
# next index and consider it as a double digit integer if it is within the range. If the s[i] == 0
# then we can't map it to any integer since we need another integer before 0. If we consider s[i] as 
# a single integer, then dp[i] = dp[i+1] since we need to know how many ways can we interprete the 
# the substring starting from i + 1. If s[i: i + 2] < 26, then we can increment dp[i] by dp[i+2] for
# a similar reason. In the end, we return dp[0] since that is the number of ways the whole string and 
# be deciphered. 

def decodeWaysRecursive(s):
    dp = {len(s) : 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == 0:
            return 0
    
        res = dfs[i+1]
        if i + 2 <= len(s) and (s[i+1] == '1' or (s[i+1] == '2' and s[i+2] in '0123456')):
            res += dfs(i+2)
        
        dp[i] = res 
        return res 

    return dfs(0)

# This is an alternate solution with the same space time complexity but more taxing on memory due
# to the load on the call stack. 

