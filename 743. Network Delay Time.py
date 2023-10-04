class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        queue = [(0, k)]
        timeElapsed = {}
        
        while queue:
            time, node = heappop(queue)
            if node not in timeElapsed:
                timeElapsed[node] = time
                if len(timeElapsed) == n:
                    return max(timeElapsed.values())
                for child, weight  in graph[node]:
                    if child not in timeElapsed:
                        heappush(queue, (time + weight, child))
        
        if len(timeElapsed) != n:
            return -1
        return max(timeElapsed.values())

                
