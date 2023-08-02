#include <string>
#include<unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t){
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s == t;
    };

    bool isAnagramLinear(string s, string t){
        unordered_map<char, int> sCount;
        unordered_map<char, int> tCount;

        if (s.length() != t.length()) return false;

        for (int i = 0; i < s.size(); i++){
            sCount[s[i]]++;
            tCount[s[i]]++;
        }

        return sCount == tCount;
    };
 
};