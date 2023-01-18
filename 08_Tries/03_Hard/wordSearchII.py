'''
Given an m x n board of characters and a list of 
strings words, return all words on the board.

Each word must be constructed from letters of sequentially 
adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be 
used more than once in a word.
'''

class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0 
        self.end = False 
    
    def addWord(self, word):
        curr = self 
        curr.count += 1 

        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
            curr.count += 1
        
        curr.end = True 
    
    def removeWord(self, word):
        curr = self 
        curr.count -= 1

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
                curr.count -= 1


def findWords(board, words):
    root = Trie()
    for w in words:
        root.addWord(w)
    
    R, C = len(board), len(board[0])
    res, seen = set(), set()

    def dfs(r, c, node, currWord):
        if r not in range(R) or c not in range(C):
            return
        if (r, c) in seen:
            return
        if board[r][c] not in node.children:
            return
        if node.children[board[r][c]].count < 1:
            return 
        
        seen.add((r, c))
        node = node.children[board[r][c]]
        currWord += board[r][c]
        if node.end:
            node.end = False 
            root.removeWord(currWord)
            res.add(currWord)
        
        dfs(r + 1, c, node, currWord)
        dfs(r - 1, c, node, currWord)
        dfs(r, c + 1, node, currWord)
        dfs(r, c - 1, node, currWord)
        seen.remove((r, c))

    for r in range(R):
        for c in range(C):
            dfs(r, c, root, "")
        
    return list(res)

# We build a trie to store all of the words efficiently. However, there is one difference
# we also store the number of words a node is present in. We also create a method to remove 
# a word which works by decreasing the count of a node. For the actual function, it works 
# very closely like the backtracking algorithm in Word Search with the difference that here
# we are traversing the trie instead of the grid. 


# Space | Time : O(mnl) | O(wl)


