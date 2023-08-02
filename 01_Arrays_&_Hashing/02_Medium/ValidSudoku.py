"""Determine if a 9 x 9 Sudoku board is valid. Only the
filled cellsneed to be validated according to the following 
rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain 
the digits 1-9 without repetition.
Note:

A Sudoku board(partially filled) could be valid but is not 
necessarily solvable. Only the filled cells need to be validated 
according to the mentioned rules.
"""
from collections import defaultdict

def main(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    sq = defaultdict(set)

    for r in range(9):
        for c in range(9):
            rq, cq = r // 3, c // 9
            if board[r][c] == ".":
                continue 

            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or 
                board[r][c] in sq[(rq, cq)]):
                return False 
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            sq[(rq, cq)].add(board[r][c])
        
    return True 

# Time | Space : O(n^2) | O(n)

            

