class UnionFind:
    def __init__(self, size):
        self.parent = {i : i for i in range(1, size+1)}
        self.rank = {i : 1 for i in range(1, size+1)}
        self.min = {i : float("inf") for i in range(1, size+1)}

    def find(self, member):
        if self.parent[member] == member:
            return member
        root = self.find(self.parent[member])
        self.parent[member] = root
    
        return root

    def union(self, x, y, cost):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX

        self.min[rootX] = min(self.min[rootX], self.min[rootY], cost)
        if rootX != rootY:
            self.rank[rootX] += self.rank[rootY]
            self.parent[rootY] = rootX

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        for n1, n2, cost in roads:
            uf.union(n1, n2, cost)
        
        return uf.min[uf.find(1)]
