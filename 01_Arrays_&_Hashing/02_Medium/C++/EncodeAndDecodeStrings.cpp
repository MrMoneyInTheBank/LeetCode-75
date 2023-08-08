#include <string>
#include <vector>

class Code {
    public:
        std::string encode(std::vector<std::string>& strs){
            std::string res = "";
            for (const string& word : strs){
                res += to_string(word.size()) + "#" + word;
            }
            return res;
        };

        std::vector<std::string> decode(std::string& s){
            std::vector<std::string> res;
            int i = 0;

            while (i < s.size()){
                int j = i;
                while (s[j] != '#'){
                    j++;
                }
                int length = stoi(s.substr(i, j - i));
                res.push_back(s.substr(j+1, length));
                i = j + 1 + length;
            }
            return res;
        };
};

// Store the length of each string before a delimiter like "#".
// Time | Space : O(n) | O(1)
