"""
Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is 
the substring of s2.
"""

from typing import List

class Solution:
    def constructHash(self, s: str) -> List[int]:
        hash_table = [0] * 26

        for c in s:
            hash_table[ord(c) - ord('a')] += 1 
        
        return hash_table

    def checkInclusionn(self, s1: str, s2: str) -> bool:
        
        freq = self.constructHash(s1)

        l, r = 0, len(s1)

        while r <= len(s2):
            if freq == self.constructHash(s2[l:r]):
                return True 
            l += 1 
            r += 1 
        
        return False 

# Time | Space : O(n^2) | O(n)

# Check is windows contains same frequencies of letters 


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         s1Count, s2Count = [0] * 26, [0] * 26
#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord("a")] += 1
#             s2Count[ord(s2[i]) - ord("a")] += 1

#         matches = 0
#         for i in range(26):
#             matches += 1 if s1Count[i] == s2Count[i] else 0

#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26:
#                 return True

#             index = ord(s2[r]) - ord("a")
#             s2Count[index] += 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:
#                 matches -= 1

#             index = ord(s2[l]) - ord("a")
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]:
#                 matches -= 1
#             l += 1
#         return matches == 26
