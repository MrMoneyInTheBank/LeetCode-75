'''
You are given a string s and an integer k. You can choose any character 
of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.
'''

from collections import defaultdict
def characterReplacement(s, k):
    count = defaultdict(int)
    res = 0 

    l = 0
    maxFreq = 0 

    for r in range(len(s)):
        count[s[r]] += 1
        maxFreq = max(maxFreq, count[s[r]])

        while (r - l + 1) - maxFreq > k:
            count[s[l]] -= 1 
            l += 1
            
        res = max(res, r - l + 1)

    return res 

# To test if a substring is valid, we need to check if the count of the majority character
# when subtracted from the length of the substring is larger than k which would allow us to 
# change all the other characters. This is why we are maintaining a maxFreq variable. 
# To actually find the substring, we use a sliding window approach. We increase the window until
# the substring is valid, at which point, we increment the left pointer. At each iteration,
# we maintain a count of the characters in a dictionary. When we are incrementing the left pointer, we
# dont need to decrement the maxFreq variable since a large result can only be found by increasing it
# and we dont need to check for a value maxFreq_i < maxFreq since we have already found a substring which 
# satisfies the property with maxFreq which is the largest substring found so far. 

# if we didn't want to use the maxFreq method, we could simply get the max from max(count.values())

# Time | Space : O(n) | O(n)
