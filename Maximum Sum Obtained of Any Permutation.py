class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7 
        n = len(nums)
        pref_sum = [0]*(n + 1)

        for start, end in requests:
            pref_sum[start] += 1
            pref_sum[end+1] -= 1

        pref_sum.pop()
        for i in range(1, n):
            pref_sum[i] += pref_sum[i-1]

        pref_sum.sort()
        nums.sort()

        result = 0
        for i in range(n):
            result += nums[i] * pref_sum[i]

        return result % MOD  
