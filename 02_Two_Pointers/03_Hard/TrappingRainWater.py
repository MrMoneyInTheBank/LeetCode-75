"""
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can 
trap after raining.
"""

def main(height):
    l, r = 0, len(height) - 1 
    leftmax, rightmax = height[l], height[r]
    res = 0 

    while l < r:
        if leftmax < rightmax:
            l += 1 
            leftmax = max(height[l], leftmax)
            res += leftmax - height[l]
        else:
            r -= 1
            rightmax = max(height[r], rightmax)
            res += rightmax - height[r]
        
    return res

# Time | Space : O(n) | O(1)
