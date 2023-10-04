class Solution:
    def maxScore(self, nums: List[int]) -> int:
        allVisited = (1 << (len(nums)+1))-1
        cache = {}

        def dp(curr, visited):
            if (curr, visited) in cache:
                return cache[(curr, visited)]
            ans = 0
            for i in range(len(nums)):
                if visited & (1 << i) == 0:
                    for j in range(len(nums)):
                        if visited & (1 << j) == 0 and i != j:
                            newVisited = visited | (1<<i)
                            newVisited = newVisited | (1 <<j)
                            ans = max(ans, curr*(math.gcd(nums[i], nums[j])) + dp(curr+1, newVisited))

            cache[(curr, visited)] = ans
            return ans

        return dp(1, 0)
