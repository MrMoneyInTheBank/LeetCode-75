#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int> nums){
        unordered_set<int> seen;

        for (const int& num : nums){
            if (seen.find(num) != seen.end()) return true;
            else seen.insert(num);
        }

        return false;
    }
};