// A phrase is a palindrome if, after converting all uppercase letters
// into lowercase letters and removing all non-alphanumeric characters,
// it reads the same forward and backward. Alphanumeric characters include
// letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

#include <string>
#include <cctype>

class Solution {
    public:
        bool isPalindrome(std::string s){
            int i = 0; 
            int j = s.size() - 1;

            while (i < j){
                while (!std::isalnum(s[i]) && i < j) i++;
                while (!std::isalnum(s[j]) && i < j) j--;

                if (std::tolower(s[i]) != std::tolower(s[j])) return false;
                i++;
                j--;
            }

            return true;
        };
};

// From the outside in, check every valid character. If unequal, return false.
// Time | Space : O(n) | O(1)
