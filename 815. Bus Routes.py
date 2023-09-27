class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for routId in range(len(routes)):
            for stop in routes[routId]:
                graph[stop].append(routId)
        
        queue = deque([source])
        visited_stops = set([source])
        visited_routes = set()
        ans = 0

        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return ans
                
                for routeId in graph[stop]:
                    if routeId not in visited_routes:
                        for next_stop in routes[routeId]:
                            if next_stop not in visited_stops:
                                queue.append(next_stop)
                                visited_stops.add(next_stop)
                        visited_routes.add(routeId)
            ans += 1
            
        return -1
