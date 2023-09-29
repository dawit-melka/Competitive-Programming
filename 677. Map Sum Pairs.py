class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.insertedWords = {}
        

    def insert(self, key: str, val: int) -> None:
        currNode = self.root
        prevWordVal = 0 
        if key in self.insertedWords:
            prevWordVal = self.insertedWords[key]
        
        for char in key:
            if char in currNode.children:
                currNode.children[char].val += val
                currNode.children[char].val -= prevWordVal
            else:
                newNode = TrieNode()
                newNode.val = val
                currNode.children[char] = newNode

            currNode = currNode.children[char]

        self.insertedWords[key] = val
        

    def sum(self, prefix: str) -> int:
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return 0
            currNode = currNode.children[char]

        return currNode.val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
