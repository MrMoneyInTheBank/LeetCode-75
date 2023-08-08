// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> res;

        for (int i = 0; i < nums.size(); i++) {
            // Avoid duplicates for the first number
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int j = i + 1;
            int k = nums.size() - 1;

            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                if (total > 0) {
                    k--;
                } else if (total < 0) {
                    j++;
                } else {
                    res.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;

                    // Avoid duplicates for the second number
                    while (j < k && nums[j] == nums[j-1]) {
                        j++;
                    }

                    // Avoid duplicates for the third number
                    while (j < k && nums[k] == nums[k+1]) {
                        k--;
                    }
                }
            }
        }
        return res;
    }
};

// The 3Sum algorithm aims to find all unique triplets in the array that sum up to zero.
// First, the array is sorted to facilitate the two-pointer approach.
// The algorithm then iterates through the array using a fixed point and employs two pointers, 'l' and 'r'.
// For each fixed point, 'l' starts right after it, and 'r' starts at the end of the array.
// If the sum of the fixed point, 'l', and 'r' is too large, 'r' is moved inwards. If too small, 'l' is moved.
// When a valid triplet is found, both 'l' and 'r' are adjusted to skip any duplicates.
// This process continues until 'l' and 'r' meet or cross, after which the next fixed point is chosen.
// By avoiding duplicate fixed points and adjusting pointers for duplicates, the algorithm ensures unique triplets.
// This method is more efficient than a brute force approach which would use three nested loops.
// Time | Space : O(n^2) | O(1)

