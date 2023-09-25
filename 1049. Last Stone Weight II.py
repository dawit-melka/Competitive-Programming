class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        dp = {}
        def dfs(i, currSum):
            if currSum >= ceil(totalSum/2) or i == len(stones):
                return abs(totalSum - currSum - currSum)
            
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            
            dp[(i, currSum)] = min(dfs(i+1, currSum+stones[i]), dfs(i+1, currSum))
            return dp[(i, currSum)]
        
        return dfs(0, 0)
