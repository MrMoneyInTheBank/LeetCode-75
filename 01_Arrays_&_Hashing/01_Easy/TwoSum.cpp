#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++){
            int comp = target - nums[i];

            if (seen.find(comp) != seen.end()) {
                return {i, seen[comp]};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};