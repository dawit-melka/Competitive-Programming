class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = collections.Counter()
        pref_sum[0] = 1
        running_sum = 0
        result = 0

        for num in nums:
            running_sum += num
            result += pref_sum[running_sum-k]
            pref_sum[running_sum] += 1
        
        return result
