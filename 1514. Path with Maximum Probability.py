class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            n1, n2 = edges[i]
            graph[n1].append((n2, succProb[i]))
            graph[n2].append((n1, succProb[i]))
        
        heap = [(-1, start_node)]
        visited = set()
        while heap:
            prob, curr_node = heappop(heap)
            if curr_node == end_node:
                return prob * -1
            visited.add(curr_node)
            for child, pr in graph[curr_node]:
                if child not in visited:
                    heappush(heap, (prob * pr, child))


        return 0
