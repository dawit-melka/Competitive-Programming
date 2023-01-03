class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None]*(n)

        for i in range(n):
            res[i] = nums[nums[i]]

        return res
