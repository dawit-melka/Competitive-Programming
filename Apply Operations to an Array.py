class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = 0
                nums[write] = temp
                write += 1

        return nums
