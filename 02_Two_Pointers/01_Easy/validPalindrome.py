'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def isValid(s):
    chars = [c.lower() for c in s if c.isalnum()]
    l, r = 0, len(chars) - 1

    while l < r:
        if chars[l] != chars[r]:
            return False
        l += 1 
        r -= 1
    
    return True 

'''
Pretty straightforward. Check from out to in. 

Time | Space: O(n) | O(n)
'''