#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k){
        unordered_map<int, int> freq;

        for (auto num : nums){
            freq[num]++;
        };

        vector<pair<int, int>> pairs(freq.begin(), freq.end());
        sort(pairs.begin(), pairs.end(), [](const pair<int, int>& a, const pair<int, int>& b){
            return a.second > b.second;
        });

        vector<int> res;
        for (int i = 0; i < k; i++){
            res.push_back(pairs[i].first);
        };

        return res;
    };
};