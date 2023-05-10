class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cycle = set()
        visited = set()
        curr_path = set()
        result = []

        def dfs(node):
            if node in curr_path or node in cycle:
                return False
            if node in visited:
                return True
            
            curr_path.add(node)
            visited.add(node)

            for ngh in graph[node]:
                if not dfs(ngh):               
                    return False
            curr_path.remove(node)
            return True
        
        for i in range(len(graph)):
            curr_path = set()
            if i not in visited:
                if not dfs(i):
                    cycle.update(curr_path)
        
        for i in range(len(graph)):
            if i not in cycle:
                result.append(i)

        return result
