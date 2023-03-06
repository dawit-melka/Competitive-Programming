class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxVal = max(nums)
        def divideSum(nums, divisor):
            runningSum = 0
            for num in nums:
                runningSum += ceil(num/divisor)
            return runningSum

        low = 0
        high = maxVal+1
        while high > low + 1:
            mid = (high + low) // 2

            currSum = divideSum(nums, mid)
            if currSum > threshold:
                low = mid
            else:
                high = mid

        return high
