class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        minVal = min(nums)
        maxVal -= k
        minVal += k
        if minVal >= maxVal:
            return 0
        return maxVal - minVal
