#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums){
        vector<int> pref;
        vector<int> suff(nums.size(), 0);
        for (int i = 0; i < nums.size(); i++){
            if (i == 0) pref.push_back(nums[0]);
            else pref.push_back(nums[i] * pref[i-1]);
        };
        for (int i = nums.size() - 1; i >= 0; i--){
            if (i == nums.size() - 1){
                suff[i] = nums[i];
            } else {
                suff[i]= nums[i]*suff[i+1];
            };
        };

        vector<int> res(nums.size(), 0);
        for (int i = 0; i < nums.size(); i++){
            if (i == 0) res[i] = suff[1];
            else if (i == nums.size() - 1) res[i] = pref[nums.size()-2];
            else {
                res[i] = pref[i-1] * suff[i+1];
            };
        };
        return res;
    };
};