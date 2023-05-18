class UnionFind:
    def __init__(self):
        self.parent = {chr(i) : chr(i) for i in range(97, 123)}
  
    def find(self, member):
        if member == self.parent[member]:
            return member

        parent = self.find(self.parent[member])
        self.parent[member] = parent
        
        return parent
    
    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)
        if parX != parY:
            self.parent[parX] = parY

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        for equation in equations:
            if equation[1] =="=":
                uf.union(equation[0], equation[3])
        
        for equation in equations:
            if equation[1] =="!" and uf.find(equation[0]) == uf.find(equation[3]):
                return False
                
        return True
     
