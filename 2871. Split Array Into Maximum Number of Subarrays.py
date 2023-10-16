class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        min_sum = nums[0]
        for num in nums:
            min_sum &= num
        if min_sum > 0:
            return 1
        
        count = 0
        running_and = nums[0]
        for i in range(len(nums)):
            running_and &= nums[i]
            if running_and == 0:
                count += 1
                if i + 1 < len(nums):
                    running_and = nums[i +1]

        return count
