class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        maxAvg = -float("inf")
        runningSum = 0

        for r in range(len(nums)):
            if r - l +1 < k:
                runningSum += nums[r]
            else:
                runningSum += nums[r]
                currAvg = runningSum / k
                maxAvg = max(maxAvg, currAvg)
                runningSum -= nums[l]
                l += 1

        return maxAvg
