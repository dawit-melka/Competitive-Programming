class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
  
    def find(self, member):
        if member == self.parent[member]:
            return member

        parent = self.find(self.parent[member])
        self.parent[member] = parent
        
        return parent
    
    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)

        if self.rank[parX] < self.rank[parY]:
            parX, parY = parX, parY

        if parX != parY:
            self.parent[parX] = parY

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        parents = {}
        result = []
        for i, j in pairs:
            uf.union(i, j)
        
        for i in range(len(s)):
            par = uf.find(i)
            if par not in parents:
                parents[par] = [0] * 26
            parents[par][ord(s[i])- ord("a")] += 1
        
        for i in range(len(s)):
            par = uf.find(i)
            for i in range(26):
                if parents[par][i] != 0:
                    parents[par][i] -= 1
                    result.append(chr(i + ord("a")))
                    break

        return "".join(result)
