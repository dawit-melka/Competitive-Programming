class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        color = [-1] * (n + 1)

        for src, dst in dislikes:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
            
        def dfs(prev, node):
            if color[node] != -1:
                return color[prev] != color[node]

            if color[prev] == -1:
                color[node] = 0
            else:
                color[node] = color[prev] ^ 1

            for nei in adj_list[node]:
                if not dfs(node, nei):
                    return False

            return True


        for i in range(1, n+1):
            if color[i] == -1:
                if not dfs(0, i):
                    return False


        return True
