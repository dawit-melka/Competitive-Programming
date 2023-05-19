class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        queue = deque()
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            indegree[node1] += 1
            indegree[node2] += 1
        
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        
        # traverse inward and minimize the height
        processed = 0
        while queue:
            if processed + len(queue) == n:
                return queue
            processed += len(queue)
            for _ in range(len(queue)):
                curr = queue.popleft()
                for ngh in graph[curr]:
                    indegree[ngh] -= 1
                    if indegree[ngh] == 1:
                        queue.append(ngh)

        return [0]

    
