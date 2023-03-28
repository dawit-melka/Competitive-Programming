class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(1, len(nums)+1):
            while nums[i-1] != i:
                if (nums[i-1] <= 0 or 
                    nums[i-1] > len(nums) or
                    nums[i-1] == nums[nums[i-1]-1]):
                    break
                
                nums[nums[i-1]-1], nums[i-1] = nums[i-1], nums[nums[i-1]-1]

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums) + 1
