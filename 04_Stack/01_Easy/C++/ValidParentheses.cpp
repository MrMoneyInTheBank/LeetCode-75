#include <unordered_map>
#include <stack>
#include <string>

class Solution{
    public:
        bool isValid(std::string s){
            std::stack<char> open;
            std::unordered_map<char, char> closeOpen = {
                {')', '('},
                {']', '['},
                {'}', '{'},
            };

            for (const char c : s){
                if (closeOpen.find(c) != closeOpen.end()){
                    if (open.empty()) return false;
                    if (open.top() != closeOpen[c]) return false;
                    open.pop();
                } else {
                    open.push(c);
                }
            }

            return open.empty();
        }
};
