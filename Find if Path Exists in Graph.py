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

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for node1, node2 in edges:
            uf.union(node1, node2)

        return uf.find(source) == uf.find(destination)
        
