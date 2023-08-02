#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs){
        unordered_map<string, vector<string>> res;

        for (string& str : strs){
            string key = str;
            sort(key.begin(), key.end());
            res[key].push_back(str);
        };

        vector<vector<string>> result;
        for (pair<const string, vector<string>>& kv : res){
            result.push_back(kv.second);
        };

        return result;
    };

private:
    vector<vector<string>> groupAnagramsQuadratic(vector<string>& strs){
        unordered_map<string, vector<string>> res;

        for (string s : strs){
            vector<int> count(26, 0);
            for (char c : s){
                count[c - 'a']++;
            };
            string key;
            for (int i : count){
                key += to_string(i) + '#';
            };

            res[key].push_back(s);
        };

        vector<vector<string>> result;
        for (pair<const string, vector<string>>& kv : res){
            result.push_back(kv.second);
        };

        return result;
    }
};