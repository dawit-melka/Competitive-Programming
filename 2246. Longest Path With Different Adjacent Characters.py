class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = {}
        for i in range(1, len(parent)):
            if parent[i] not in adj:
                adj[parent[i]] = []
            adj[parent[i]].append(i)
        self.result = 1
        
        def dfs(node):
            if node not in adj:
                return 1
            maxChilds = [0, 0]
            for child in adj[node]:
                maxChildLen = dfs(child)
                if s[child] != s[node]:
                    maxChilds.append(maxChildLen)
                    maxChilds.sort()
                    maxChilds.pop(0)
                    
            self.result = max(self.result, sum(maxChilds)+1)

            return max(maxChilds)+1
        
        dfs(0)
        return self.result
            
