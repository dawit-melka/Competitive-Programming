class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
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
        
    
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        hamDis = 0
        groups = defaultdict(Counter)
        uf = UnionFind(len(target))
        
        for i, j in allowedSwaps:
            uf.union(i, j)
        
        for i in range(len(source)):
            parent = uf.find(i)
            groups[parent][source[i]] += 1

        for i in range(len(target)):
            parent = uf.find(i)
            val = target[i]
            if val not in groups[parent] or groups[parent][val] == 0:
                hamDis += 1
            else:
                groups[parent][val] -= 1
                

        return hamDis
