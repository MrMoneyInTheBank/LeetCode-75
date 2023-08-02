#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums){
        unordered_set<int> unique;
        int longest = 0;

        for (int num : nums){
            if (unique.find(num - 1) == unique.end()){
                int l = 0;
                while (unique.find(num + 1) != unique.end()){
                    l++;
                };
                longest = max(longest,l);
            };
        };

        return longest;
    };
};