class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.count = size
    
    def find(self, member):
        root = member
        while root != self.parent[root]:
            root = self.parent[root]

        while member != root:
            parent = self.parent[member]
            self.parent[member] = root
            member = parent
        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
        else:
            return [x, y]
        return None
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for n1, n2 in edges:
            if uf.union(n1-1, n2-1):
                return [n1, n2]
