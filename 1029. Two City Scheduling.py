class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        cache = {}
        def dfs(i, city_A_count, city_B_count):
            if (i, city_A_count, city_B_count) in cache:
                return cache[(i, city_A_count, city_B_count)]
            if city_A_count > n or city_B_count > n:
                return float("inf")
            if i == 2*n:
                return 0
            
            cache[(i, city_A_count, city_B_count)] = min(costs[i][0] + dfs(i+1, city_A_count+1, city_B_count), costs[i][1] + dfs(i+1, city_A_count, city_B_count+1))

            return cache[(i, city_A_count, city_B_count)]
        
        return dfs(0, 0, 0)
