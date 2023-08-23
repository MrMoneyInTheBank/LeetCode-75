#include <string>
#include <unordered_map>

class Solution {
public:
    std::string minWindow(std::string s, std::string t) {
        
        auto inside = [](const std::unordered_map<char, int>& charCount, const std::unordered_map<char, int>& window) {
            for (const auto& [key, value] : charCount) {
                if (window.find(key) == window.end() || window.at(key) == 0 || window.at(key) < value) {
                    return false;
                }
            }
            return true;
        };

        std::unordered_map<char, int> tCount;
        for (char charT : t) {
            tCount[charT]++;
        }

        std::unordered_map<char, int> windowCount;
        std::string res = "";
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            windowCount[s[r]]++;

            while (inside(tCount, windowCount)) {
                windowCount[s[l]]--;
                l++;

                if (res == "" || res.length() > r - l + 2) {
                    res = s.substr(l - 1, r - l + 2);
                }
            }
        }

        return res;
    }
};
