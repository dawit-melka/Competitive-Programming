class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        dp = [float("inf")] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])
