class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # build graph
        # count frequency of nodes in paths
        # find the minimum possible answer (using dp)

        graph = defaultdict(list)

        def bfs(start, end):
            queue = deque([(start, [start])])
            visited = set([start])
            while queue:
                node, path = queue.popleft()
                if node == end:
                    return path
                
                for ngh in graph[node]:
                    if ngh not in visited:
                        queue.append((ngh, path + [ngh]))
                        visited.add(ngh)

        cache = {}
        def dp(node, parent, canHalf):
            if (node, parent, canHalf) in cache:
                return cache[(node,parent,canHalf)]
            if canHalf:
                cost = nodeCount[node] * price[node] // 2
            else:
                cost = nodeCount[node] * price[node]
            
            for ngh in graph[node]:
                if ngh != parent:
                    if canHalf:
                        nghCost = dp(ngh, node, False)
                    else:
                        nghCost = min(dp(ngh, node, True), dp(ngh, node, False))
                    cost += nghCost
            cache[(node,parent,canHalf)] = cost
            return cost


        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        nodeCount = defaultdict(int)
        
        for s, e in trips:
            path = bfs(s, e)
            for node in path:
                nodeCount[node] += 1
        
        minCost = float("inf")
        for node in range(n):
            minCost = min(minCost, dp(node, None, True), dp(node, None, False))

        return minCost
