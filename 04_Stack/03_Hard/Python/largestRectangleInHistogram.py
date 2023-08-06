"""
Given an array of integers heights representing the histogram's bar 
height where the width of each bar is 1, return the area of the largest 
rectangle in the histogram.
"""

def largestRectangleArea(heights):
    maxArea = 0
    stack = []  # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea

# Time | Space : O(n) | O(n)

# When you come across a block, if there is a taller block to the after it 
# then we know that we can't extend this block's height further to create a 
# different rectangle. We can do this if there is a taller block ahead. The 
# idea is to go through the blocks and add them to a stack with the index that 
# we can consider them from and the height. Once we reach a block such that 
# the top of the stack can't be extended further, we calculate the area that 
# can be made with the block until now and do so until all blocks which can 
# be extended remain in the stack. Once we have popped the blocks we can't 
# consider, when we add the the stack the current block,we need to make sure 
# to add the correct starting index which is the index of the last block with 
# a satisfactory height. After going through all the blocks, whichever blocks 
# are still left in the stack can be extended all the way to the end from where 
# the start with whatever height they have so we calculate this area again. 
# Throughout this whole process, we keep track of the maxArea that we can form.