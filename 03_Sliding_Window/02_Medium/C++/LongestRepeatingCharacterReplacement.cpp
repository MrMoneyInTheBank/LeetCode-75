#include <unordered_map>
#include <string>
#include <algorithm>

class Solution{
    public:
        int characterReplacement(std::string s, int k){
            std::unordered_map<char, int> count;
            int l = 0, res = 0, maxFreq = 0;

            for (int r = 0; r < s.length(); r++){
                count[s[r]]++;
                maxFreq = std::max(maxFreq, count[s[r]]);

                while ((r - l + 1) - maxFreq > k){
                    count[s[l]]--;
                    l++;
                }
                res = std::max(res, r - l + 1);
            }

            return res;
        }
};
