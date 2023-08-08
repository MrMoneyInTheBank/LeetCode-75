/*
Given an array of string strs, group the anagrams together. 
You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all
the original letters exactly once.
*/

#include <vector>
#include <string>
#include <unordered_map>

class Solution{
    public:
        std::vector<vector<string>> groupAnagrams(std::vector<std::string>& strs){
            std::unordered_map<std::string, std::vector<std::string>> hashmap;
            for (const std::string word : strs){
                std::string key = getKey(word);
                hashmap[key].push_back(word);
            }

            std::vector<std::vector<std::string>> res;
            for (auto& kv : hashmap){
                res.push_back(kv.second);
            }

            return res;
        }
    private:
        std::string getKey(std::string str){
            std::vector<int> count(26, 0);
            for (const char c : str){
                count[c - 'a']++;
            }
            
            std::string key = "";
            for (const int num : count){
                key.append(to_string(num + 'a'));
            }
            return key;
        }
};

// A property of anagrams is that the letter frequency of each word/phrase is the same.
// Using this, we can create a hashmap where the keys if the letter frequency, and the values
// are all the words which share that letter frequency. In the end, we can return the values
// of this hashmap.

// Time | Space : O(n * m) | O(n * m)