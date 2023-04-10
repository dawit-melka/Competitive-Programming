class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []
        path = [0]

        def dfs(node):
            if node == len(graph)-1:
                all_paths.append(path.copy())

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()

        dfs(0)

        return all_paths
