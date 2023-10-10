class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for src1, dst1, c in flights:
            graph[src1].append((dst1, c))
        queue = [(0, 0, src)]
        visited = defaultdict(int)
        visited[src] = 0 
        
        while queue:
            stops, price,city = heappop(queue)
            if stops > k:
                break
            
            for ngh, cost in graph[city]:
                if ngh not in visited or visited[ngh] > price + cost:
                    visited[ngh] = price + cost
                    heappush(queue, (stops+1,price + cost, ngh))
        
        return visited[dst] if dst in visited else -1
