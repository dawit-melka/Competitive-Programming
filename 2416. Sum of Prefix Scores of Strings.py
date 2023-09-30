# Approach 1: Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
            currNode.count += 1
    
    def findPrefixScore(self, word):
        count = 0
        currNode = self.root
        
        for char in word:
            currNode = currNode.children[char]
            count += currNode.count
        
        return count
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        result = []
        for word in words:
            trie.insert(word)
        
        for word in words:
            result.append(trie.findPrefixScore(word))
        
        return result

# Approach 2: Two pointers
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        sortedWords = sorted(words)
        result = []
        def findAns(word):
            l = 0
            r = len(words)-1
            ans = 0
            for i in range(len(word)):
                while l <= r and(len(sortedWords[l]) <= i or sortedWords[l][i] != word[i]):
                    l += 1
                while r >= l and(len(sortedWords[r]) <= i or sortedWords[r][i] != word[i]):
                    r -= 1
                if r < l:
                    break
                else:
                    ans +=( r - l + 1)
            
            return ans
         
        for word in words:
            result.append(findAns(word))
            
        return result
