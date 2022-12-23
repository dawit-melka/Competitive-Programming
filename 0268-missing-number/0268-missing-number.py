class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_0_to_n = n*(n+1)//2
        
        for val in nums:
            sum_0_to_n -= val
        
        return sum_0_to_n