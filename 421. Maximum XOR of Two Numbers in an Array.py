# Approach 1: Trie
class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self, maxBit):
        self.root = TrieNode()
        self.maxBit = maxBit

    def insert(self, num):
        currNode = self.root
        for i in range(self.maxBit, -1, -1):
            currBit = (num >> i) & 1
            if currBit not in currNode.children:
                currNode.children[currBit] = TrieNode()
            currNode = currNode.children[currBit]

    def findMaxXOR(self, num):
        currNode = self.root
        xor = 0
        for i in range(self.maxBit, -1, -1):
            currBit = (num >> i) & 1
            complement = 1 - currBit
            if complement in currNode.children:
                xor |= (1 << i)
                currNode = currNode.children[complement]
            else:
                currNode = currNode.children[currBit]
        
        return xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxBit = 0
        for num in nums:
            count = 0
            while num:
                count += 1
                num = num >> 1
            maxBit = max(maxBit, count)

        trie = Trie(maxBit)
        maxXOR = 0
        for num in nums:
            trie.insert(num)
            maxXOR = max(maxXOR, trie.findMaxXOR(num))
        
        return maxXOR

# Approach 2: Optimized complex solution
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, output = 0, 0
        for i in range(31,-1,-1):
            mask |= (1<<i)
            found = set([n & mask  for n in nums])

            temp = output | 1 << i
            for f in found:
                if f ^ temp in found:
                    output = temp
        
        return output
