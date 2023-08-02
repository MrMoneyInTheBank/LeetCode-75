class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root 

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        
        curr.end = True 

    def search(self, word: str) -> bool:
        curr = self.root 

        for char in word:
            if char not in curr.children:
                return False 
            curr = curr.children[char]
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:

        curr = self.root 

        for char in prefix:
            if char not in curr.children:
                return False 
            curr = curr.children[char]
        
        return True 

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)

# Each node will have a boolean value representing whether or not it is the end of a word 
# and a dictionary which holds all of its children nodes which will be tree nodes themselves
# The root is initialized to be an empty node. To insert a letter, if the letter is already 
# a child of the parent node, we don't to anything. Else we create a key with the child node. 
# To search for a word of prefix, we traverse through the node and its children. If we dont find
# a node at any point, we return False. We return True for the prefix and return True if the current
# node is the end of a word for the word serach.


# Time | Space: O(n) | O(n) 
