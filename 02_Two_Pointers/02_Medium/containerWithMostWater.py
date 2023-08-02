'''
You are given an integer array height of length n. There are n vertical lines drawn
 such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

def maxArea(height):
    l, r = 0, len(height) - 1
    area = 0

    while l < r:
        area = max(area, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return area


# The area will be the width times the minimum of the heights of either boundary 
# At each iteration, always change the pointer to the smaller height to possible 
# find a bigger height which might compensate for the change in width since the 
# change is width is constant. Keep track of the max area at each itertation. 

# Time | Space: O(n) | O(1)
