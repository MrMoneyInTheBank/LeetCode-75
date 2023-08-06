/*
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add 
up to target.

You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

You can return the answer in any order.
*/

#include <vector>
#include <unordered_map>

class Solution{
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target){
        std::unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++){
            int comp = target - nums[i];
            if (seen.find(comp) != seen.end()){
                std::vector<int> res = {seen[comp], i};
                return res;
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};

// Traverse through the array while storing the numbers already 
// seen in a diciontary mapping them to their indices. For each 
// number in the array, if the complement has already been seen, 
// then we can return the current index and the value of the complement
// stored in the dictionary. Otherwise we add the current number and
// index to the dicitonary. 

// Time Complexity: O(n)
// Space Complexity: O(n)
