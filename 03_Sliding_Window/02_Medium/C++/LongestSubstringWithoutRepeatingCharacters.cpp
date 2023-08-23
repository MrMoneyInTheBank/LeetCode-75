#include <string>
#include <unordered_set>
#include <algorithm>

class Solution{
    public:
        int lengthOfLongestSubstring(std::string s){
            if (s == "") return 0;

            int res = 0;
            int l = 0;
            std::unordered_set<char> seen;

            for (int r = 0; r < s.length(); r++){
                if (seen.find(s[r]) == seen.end()){
                    seen.insert(s[r]);
                    res = std::max(res, r - l + 1);
                } else {
                    while (seen.find(s[r]) != seen.end()){
                        seen.erase(s[l]);
                        l++;
                    }
                    seen.insert(s[r]);
                }
            }

            return res;
        }
};
