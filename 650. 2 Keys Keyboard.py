class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0]*(n + 2)
        for i in range(2,n+1):
            dp[i] = i
            for j in range(1, i):
                # find the factors
                if i%j == 0:
                    # <dp[i//j] + j> min operations needed plus how many times it repeats
                    dp[i] = min(dp[i], dp[i//j] + j)
        
        return dp[n]

