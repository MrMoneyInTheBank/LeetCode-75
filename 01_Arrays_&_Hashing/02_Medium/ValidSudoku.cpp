#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool validSudoku(vector<vector<char>>& board){
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<string, unordered_set<char>> sq;

        for (int row = 0; row < 9; row++){
            for (int col = 0; col < 9; col++){
                if (board[row][col] == '.') continue;

                char curr = board[row][col];
                string square = to_string(row/3) + "-" + to_string(col/3);

                if (rows[row].find(curr) != rows[row].end()) return false;
                if (cols[row].find(curr) != cols[row].end()) return false;
                if (sq[square].find(curr) != sq[square].end()) return false;

                rows[row].insert(curr);
                cols[col].insert(curr);
                sq[square].insert(curr);
            };
        };
        return false;
    };
};