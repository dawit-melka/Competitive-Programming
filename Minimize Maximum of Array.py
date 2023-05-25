class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        runningSum = 0
        result = float("-inf")
        
        for i in range(len(nums)):
            runningSum += nums[i]
            result = max(result, ceil(runningSum / (i + 1)))
        
        return result
