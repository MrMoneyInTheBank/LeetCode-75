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


print(main([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
