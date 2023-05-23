class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1 for i in range(size)]
    
    def find(self, member):
        if member == self.parent[member]:
            return member
        parent = self.find(self.parent[member])
        self.parent[member] = parent
        
        return parent

    def union(self, x, y):
        parX = self.find(x)
        parY = self.find(y)

        if self.size[parX] < self.size[parY]:
            parX, parY = parY, parX
        
        if parX != parY:
            self.parent[parY] = parX
            self.size[parX] += self.size[parY]
            return True
        
        return False
    
class Solution:
    def manhattanDistance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(len(points))
        allEdges = []
        total = 0

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                allEdges.append((self.manhattanDistance(points[i], points[j]), i, j))


        allEdges.sort()

        for idx in range(len(allEdges)):
            cost, i, j = allEdges[idx]
            if uf.union(i, j):
                total += cost

        return total
