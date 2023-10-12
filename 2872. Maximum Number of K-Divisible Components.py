class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.count = 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(parent, node):
            if parent != -1 and len(graph[node]) == 1:
                return values[node]

            child_sum = 0
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                curr_child_sum = dfs(node, neighbour)
                if curr_child_sum == -1:
                    continue
                if curr_child_sum % k == 0:
                    self.count += 1
                else:
                    child_sum += curr_child_sum
            child_sum += values[node]
            if child_sum % k == 0:
                self.count += 1
                return -1
            else:
                return child_sum

        dfs(-1, 0)
        return self.count
        
