'''
Write a function that takes an unsigned integer and returns 
the number of '1' bits it has (also known as the Hamming weight).
'''


def hammingWeight(n):
    res = 0

    while n:
        res += n & 1
        n = n >> 1

    return res

# We use the and operator to check the least significant binary digit of n.
# If if it one, then the and operator will return one else zero. Next, we
# shift all the bits to the right by one.

# Time | Space: O(1) | O(1)
# Constant complexity since integers are 32bits at most
