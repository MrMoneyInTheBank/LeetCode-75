"""
Given a string s and a dictionary of strings wordDict, return true if s can 
be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the 
segmentation.

"""

def wordBreak(s, wordDict):

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]

# Time | Space : O(n^3) | O(n)

# If we work backwards, we can successively find if there are any substrings present in the dicitonary. 
# After this, we can mark True can from the current position onwards, the substring can be broken up. 
# If we keep iterating backwards, and find that there exists a word in wordDict such that dp[i + len(word)] == True
# then we know that s[i:] can be broken down. We extend this until we reach i = 0 and return dp[0]
# The two for loops make this quadratic and the string comparison is linear therefore the function is 
# cubic in complexity. 