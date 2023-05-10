class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        todo = deque()
        result = [set() for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            indegree[dst] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                todo.append(i)
        
        while todo:
            curr = todo.popleft()
            for ngh in graph[curr]:
                indegree[ngh] -= 1
                result[ngh].update(result[curr])
                result[ngh].add(curr)
                
                if indegree[ngh] == 0:
                    todo.append(ngh)
                
        
        for i in range(n):
            result[i] = sorted(result[i])
        
        return result
