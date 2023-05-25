class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0
        nums.sort()
        result = float("inf")
        result = min(result, nums[n-4] - nums[0])
        result = min(result, nums[n-3] - nums[1])
        result = min(result, nums[n-2] - nums[2])
        result = min(result, nums[n-1] - nums[3])

        return result
