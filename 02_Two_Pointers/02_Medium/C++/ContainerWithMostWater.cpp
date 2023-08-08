// You are given an integer array height of length n. There are n vertical
// lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container, such that 
// the container contains the most water.

// Return the maximum amount of water a container can store.

// Notice that you may not slant the container.


#include <vector>

class Solution{
    public:
        int maxArea(std::vector<int>& height) {
            int l = 0, r = height.size() - 1;
            int res = 0;

            while (l < r){
                int currArea = (r - l) * min(height[l], height[r]);
                res = max(res, currArea);

                if (height[l] <= height[r]) l++;
                else r--;
            }
            
            return res;
        };
};

// Using two pointers, calculate the area using (r-l)*min(height[l], height[r]) since this is 
// the rectangle we can create with the given heights. Move the lower height since this ensures that
// the area is now minimized
//
// Time | Space : O(n) | O(1)
