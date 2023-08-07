/*
 * Given an array of numbers, return True if there is a duplicate
 * number in the array. Return False is otherwise.
 */

#include <vector>
#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums){
        std::unordered_set<int> seen;

        for (const int num : nums){
            if (seen.find(num) != seen.end()) return true;
            else seen.insert(num);
        }
        return false;
    };
};

// Construct a hashset and add numbers from the array into the set.
// If a number already exists in the set, we can return true. If we 
// can loop through the entire array but still not catch a duplicate, 
// we return false
//
// Time | Space : O(n) | O(n)
