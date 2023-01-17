'''
Write a function that takes an unsigned integer and returns 
the number of '1' bits it has (also known as the Hamming weight).
'''

def hammingWeight(n):
    res = 0 

    while n:
        res += n % 2
        n = n >> 2
    
    return res 

# Since the number is stored in binary, we just check the least siginificant digit
# to see if it is a one or not, increment the count accordingly, and shift all the bits
# to the right

# Time | Space: O(1) | O(1) 
# Constant complexity since integers are 32bits at most 
