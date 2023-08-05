"""
Given an integer n, return an array ans of length n + 1 such that 
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary 
representation of i.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0] * (n+1)
        res[1] = 1

        offset = 1

        for i in range(2, n+1):
            if offset * 2 == i:
                offset = i

            res[i] = 1 + res[i-offset]

        return res

# Time | Space : O(n) | O(n)

# In binary numbers, we observe a pattern where the number of ones ("hamming weight") cycles until the next powers of two,
# similar to how base-10 numbers cycle every tenth number. First, we handle the special case when the input is 0, where the
# hamming weight is also 0. We return a list containing only 0 in this case. Next, we initialize a result list with the first
# two elements, [0, 1], representing the hamming weights for the numbers 0 and 1. We introduce an offset variable, initially
# set to 1. This offset helps us determine when to update the hamming weight based on the powers of two. Starting from the
# number 2, we iterate up to the specified number, inclusively. For each iteration, we check if the current index (i) is equal
# to the double of the offset. If it is, it means we have reached the next power of two. When we encounter the next power of two,
# we update the offset to the current index (i). This signifies that we will be cycling through the digits until the next power of
# two. To calculate the hamming weight for the current index (i), we add 1 to the hamming weight of the previous cycle (i-offset)
# and append it to the result list. Finally, we return the complete result list containing the hamming weights for all the numbers
# from 0 to the specified number, inclusive.
