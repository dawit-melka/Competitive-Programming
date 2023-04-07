class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        adj_list = defaultdict(list)
        visited = set()

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c]:
                    adj_list[r].append(c)

        def dfs(city):
            if city in visited:
                return

            visited.add(city)

            for neighbour in adj_list[city]:
                dfs(neighbour)

        for city in range(len(isConnected)):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces
