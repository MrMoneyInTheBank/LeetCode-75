"""
Reverse bits of a given 32 bits unsigned integer.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res |= (bit << (31 - i))

        return res

# Time | Space : O(1) | O(1)
# Constant complexity since we know the input is capped

# Getting the value of each bit in the input is not difficult. We can just use the logic and
# operator and then shift all the bits in input to the right by one. The tricky part is writing
# them in reverse. For this, we initialize an emtpty 32-bit memory address. We then use logic or
# with the bit value and the result. But we make sure the shift the bit value to the left by 31 minus
# its current position in the original input. We return the result at the end.
