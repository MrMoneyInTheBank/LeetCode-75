/*
 * Given two strings s and t, return true if t is an anagram of s, and 
 * false otherwise.
 *
 * An anagram is a word or a phrase formed by rearranging the letters
 * of a different word of phrase, typically using all original letters
 * exactly once
 */

#include <string>
#include <unordered_map>

class Solution {
public:
    bool isAnagram(std::string& t, std::string& s){
        if (t.length() != s.length()) return false;

        std::unordered_map<char, int> tCount;
        std::unordered_map<char, int> sCount;
    
        for (int i = 0; i < t.length(); i++){
            char t1 = t[i];
            char s1 = s[i];
            tCount[t1]++;
            sCount[s1]++;
        };
        
        return tCount == sCount ? true : false;
    };
};

// Construct two hashmaps which hold the letter frequencies of the two
// words. Anagrams have an identical letter frequency due to their 
// construction. After creating the hashmap, check if they are equal
// or not. 
//
// Time | Space: O(n) | O(n) 
//
// Alternate Solution
// 
// #include <string>
// #include <algorithm>
//
// bool isAnagram(std::string& s, std::string& t){
//     std::sort(s.begin(), s.end());
//     std::sort(t.begin(), t.end());
//     return s == t;
// };
