class TrieNode:
  def __init__(self):
    self.children = {}
    self.index = []

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word, i):
    currNode = self.root
    for char in word:
      if char not in currNode.children:
        currNode.children[char] = TrieNode()
      currNode = currNode.children[char]
      currNode.index.append(i)
  
  def insertReverse(self, word, i):
    currNode = self.root
    for j in range(len(word)-1, -1, -1):
      char = word[j]
      if char not in currNode.children:
        currNode.children[char] = TrieNode()
      currNode = currNode.children[char]
      currNode.index.append(i)

  def startsWith(self, pref):
    currNode = self.root
    for char in pref:
      if char not in currNode.children:
        return []
      currNode = currNode.children[char]

    return currNode.index
  
  def endsWith(self, suf):
    currNode = self.root
    for i in range(len(suf)-1, -1, -1):
      char = suf[i]
      if char not in currNode.children:
        return []
      currNode = currNode.children[char]

    return currNode.index

class WordFilter:

    def __init__(self, words: List[str]):
      self.prefTrie = Trie()
      self.sefTrie = Trie()
      for i in range(len(words)):
        self.prefTrie.insert(words[i], i)
        self.sefTrie.insertReverse(words[i], i)
        

    def f(self, pref: str, suff: str) -> int:
        prefIdxs = self.prefTrie.startsWith(pref)
        suffIdxs = self.sefTrie.endsWith(suff)
        p = len(prefIdxs)-1
        s = len(suffIdxs)-1
        while p >= 0 and s >= 0:
          if prefIdxs[p] == suffIdxs[s]:
            return prefIdxs[p]
          elif prefIdxs[p] > suffIdxs[s]:
            p -= 1
          else:
            s -= 1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
