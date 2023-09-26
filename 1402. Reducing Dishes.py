class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo = {}
        def dp(mult, i):
            if i == len(satisfaction):
                return 0
            if (mult, i) not in memo:
                if satisfaction[i] < 0:
                    memo[(mult,i)]= max(satisfaction[i]*mult+dp(mult+1, i+1), dp(mult, i+1))
                else:
                    memo[(mult,i)]=  satisfaction[i]*mult+dp(mult+1, i+1)
            return memo[(mult,i)]

        return dp(1, 0)
