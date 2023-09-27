class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for[n1, n2] in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        def dfs(prev, node):
            childs_time_taken = 0
            for child in graph[node]:
                if child != prev:
                    childs_time_taken += dfs(node, child)
            if node == 0:
                return childs_time_taken
            if childs_time_taken > 0:
                return childs_time_taken + 2
            if hasApple[node]:
                return 2
            return 0

        return dfs(-1, 0)
