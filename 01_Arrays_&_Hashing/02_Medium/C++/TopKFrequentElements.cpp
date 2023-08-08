// Given an integer array nums and an integer k, return the k most 
// frequent elements. You may return the answer in any order.

#include <vector>
#include <unordered_map>
#include <algorithm>


class Solution{
    public:
        std::vector<int> topKFrequent(std::vector<int>& nums, int k){
            std::unordered_map<int, int> freq;

            for (const int num : nums){
                freq[num]++;
            };

            std::vector<std::pair<int, int>> count(freq.begin(), freq.end());
            std::sort(count.begin(), count.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b){ return a.second > b.second;});

    
            std::vector<int> res;
            for (int i = 0; i < k; i++){
                res.push_back(count[i].first);
            };
            return res;
        };
};

// Create a hashmap which counts the frequency of each element. 
// Sort this hashmap in decreasing order. Then add the first k
// elements into a result vector and return that result vector.
//
// Time | Space : O(n log(n)) | O(n)
