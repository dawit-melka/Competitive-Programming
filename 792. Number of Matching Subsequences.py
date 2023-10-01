class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.isEnd = True
        currNode.count += 1
    
    def dfs(self, node, word, i):
        for char in node.children:
            childNode = node.children[char]
            idx = i
            while idx < len(word) and word[idx] != char:
                idx += 1
            if idx < len(word):
                if childNode.isEnd:
                    self.count += childNode.count
                
                self.dfs(childNode, word, idx+1)
    
    def countMatching(self, word):
        self.count = 0
        self.dfs(self.root, word, 0)
        return self.count

        

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.countMatching(s)
        
