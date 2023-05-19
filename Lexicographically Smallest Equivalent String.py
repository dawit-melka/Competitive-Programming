class UnionFind:
    def __init__(self):
        self.parent = {chr(i) : chr(i) for i in range(97, 123)}
        self.min = {chr(i) : chr(i) for i in range(97, 123)}
        self.rank = {chr(i) : 1 for i in range(97, 123)}
    
    def find(self, char):
        if char == self.parent[char]:
            return char
        parent = self.find(self.parent[char])
        self.parent[char] = parent

        return parent
    
    def union(self, letter1, letter2):
        root1 = self.find(letter1)
        root2 = self.find(letter2)

        if self.rank[root1] < self.rank[root2]:
            root1, root2 = root2, root2
        
        if root1 != root2:
            self.min[root1] = min(self.min[root1], self.min[root2])
            self.parent[root2] = root1
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        result = []
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        for char in baseStr:
            result.append(uf.min[uf.find(char)])
        
        return "".join(result)
