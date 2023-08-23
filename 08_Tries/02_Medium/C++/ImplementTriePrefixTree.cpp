#include <string>
#include <vector>

struct TrieNode{
    TrieNode* children[26];
    bool isWord;

    TrieNode(){
        for (int i = 0; i < 26; i++){
            children[i] = NULL;
        }
        isWord = false;
    };
};

class Trie{
    public:
        Trie(){
            root = new TrieNode();
        }

        void insert(std::string word){
            TrieNode* node = root;
            int index = 0;

            for (int i = 0; i < word.size(); i++){
                index = word[i] - 'a';
                if (node->children[index] == NULL){
                    node->children[index] = new TrieNode();
                }
                node = node->children[index];
            }
            node->isWord = true;
        }

        bool search(std::string word){
            TrieNode* node = root;
            int index = 0;

            for (int i = 0; i < word.size(); i++){
                index = word[i] - 'a';
                if (node->children[index] == NULL) return false;
                node = node->children[index];
            }
            return node->isWord;
        }

        bool startsWith(std::string word){
            TrieNode* node = root;
            int index = 0;

            for (int i = 0; i < word.size(); i++){
                index = word[i] - 'a';
                if (node->children[index] == NULL) return false;
                node = node->children[index];
            }
            return true;
        }
    private:
        TrieNode* root;
};        
