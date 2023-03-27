class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return[nums[i], i + 1]

        return
