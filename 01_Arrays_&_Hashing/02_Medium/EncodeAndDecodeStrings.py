class Solution:
    '''
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string
    '''

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res 
    
    '''
    @param: s: A string
    @return: decodes a single string into a list of strings
    '''

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = 0 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        
        return res 

# store length of str before each string and delimiter like '#';
# Space | Time: O(n) | O(n)