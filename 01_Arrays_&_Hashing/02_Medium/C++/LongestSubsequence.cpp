// Given an unsorted array of integers nums, return the length of the 
// longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

#include <unordered_set>

class Solution {
    public:
        int longestConsecutive(std::vector<int>& nums){
            std::unordered_map<int> unique(nums.begin(), nums.end());
            int longest = 0;

            for (const int num : unique){
                if (unique.find(num-1) == unique.end()){
                    int l = 0;
                    while (unique.find(num + l) != unique.end()){
                        l++;
                    }
                    longest = max(longest, l);
                }
            }
            return longest;
        };
};

// For the starting point of a sequence, the number before it must not be present in the 
// input vector. To find all the unique elements, we create a hashset. Then we loop over
// all the unique numbers. If it is a starting point, we try to extend this sequence
// by continously checking if the next number is in the hashset. In the end, we return
// the longest sequence we can find.
//
// Time | Space : O(n) | O(n)

