"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)
"""
import math 

class Solution:
    def reverse(self, x: int) -> int:

        MIN = -(2**31)  
        MAX = 2**31 - 1 

        res = 0
        while x:
            digit = int(math.fmod(x, 10))  
            x = int(x / 10)  

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res

# Time | Space: O(n) | O(1)

# Reversing an integer is easy. Take the last digit with mod 10, integer divide by 10 to chop it off
# and then multiply res by 10 and add digit. The interested part comes because of the bounds. If res is already
# out of bounds (res >> MAX//10 || res < MIN // 10), then return 0. Else, if res == MIN // 10 || res == MAX // 10
# and the last digit makes it go out of bounds, then return 0. Otherwise, return the reverse.