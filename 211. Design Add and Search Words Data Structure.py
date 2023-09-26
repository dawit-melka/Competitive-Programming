class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.root
        for char in word:
            if char not in trie.children:
                trie.children[char] = TrieNode()
            trie = trie.children[char]
        trie.is_end = True

    def search(self, word: str) -> bool:
        def dfs(trie, index):
            if index == len(word):
                return trie.is_end
            if word[index] == '.':
                for child in trie.children:
                    if dfs(trie.children[child], index+1):
                        return True
                return False
            else:
                if word[index] not in trie.children:
                    return False
                return dfs(trie.children[word[index]], index+1)
        
        return dfs(self.root, 0)
