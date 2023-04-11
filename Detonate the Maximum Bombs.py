class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for i in range(len(bombs)):
            curr = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                dx = bombs[j][0] - bombs[i][0]
                dy = bombs[j][1] - bombs[i][1]
                r1, r2 = bombs[i][2], bombs[j][1]
                distance = math.sqrt(dx**2 + dy**2)

                if distance <= r1:

                    adj_list[i].append(j)                

        visited = set()

        def dfs(curr_bomb):
            if curr_bomb in visited:
                return 0

            visited.add(curr_bomb)
            curr_count = 0

            for nei in adj_list[curr_bomb]:
                curr_count += dfs(nei)
            

            return 1 + curr_count

        result = 0   
        for i in range(len(bombs)):
            visited = set()
            result = max(result, dfs(i))

        return result


