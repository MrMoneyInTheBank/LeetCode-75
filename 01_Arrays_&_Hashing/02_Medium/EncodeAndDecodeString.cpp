#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string encode(vector<string>& strs){
        string res;

        for (const string& s : strs){
            int num = s.size();
            string len = to_string(num);
            res = res + len + "#" + s;
        };

        return res;
    };

    vector<string> decode(string& str) {
        int i = 0;
        vector<string> res;

        while (i < str.size()){
            int j = i;
            while (str[j] != '#'){
                j++;
            }
            int len = stoi(str.substr(i, j - 1));
            res.push_back(str.substr(j+1, len));
            i = j + 1 + len;
        };

        return res;
    };
};