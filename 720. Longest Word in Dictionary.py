class TrieNode:
    def __init__(self):
        self.children = {}
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
    

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(node):
            ans = ""
            for child in node.children:
                if node.children[child].isEnd:
                    curr = child + dfs(node.children[child])
                    if len(curr) > len(ans):
                        ans = curr
                    elif len(curr) == len(ans) and curr < ans:
                        ans = curr
            
            return ans

        return dfs(trie.root)    
        
