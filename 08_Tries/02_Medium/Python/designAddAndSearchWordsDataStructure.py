'''
Design a data structure that supports adding new words and finding 
if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.

void addWord(word) Adds word to the data structure, it can be matched later.

bool search(word) Returns true if there is any string in the data structure 
that matches word or false otherwise. word may contain dots '.' where dots 
can be matched with any letter.
'''




class Node:
    def __init__(self):
        self.children = {}
        self.end = False 
    

class WordDictionary:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        curr = self.root 

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            
            curr = curr.children[c]
        
        curr.end = False 
    
    def search(self, word):
        def dfs(i, root):
            curr = root 
        
            for j in range(i, len(word)):
                c = word[j] 

                if c == '.':
                    for child in curr.children.values():
                        if dfs(j+1, word):
                            return True 
                        
                    return False 
                else:
                    if c not in curr.children:
                        return False 
                    curr = curr.children[c]
                
            return curr.end 
        
        return dfs(0, self.root)
    
# This is essentially just the implementation of a trie data structure. Adding new words 
# is exactly the same as how new words are added to a trei. If there are no "." in a word
# then the search is done exactly the same as well. However, if there is a ".", we need to check 
# every possible child of the current node for the subsequence letters. This is done by the dfs 
# function. If there is no solution in any paths, then we return False otherwise we have found 
# all the letters and now we just need to confirm whether or not it is the end of a word. 

# Time | Space: O(n) | O(n) 
