class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0]*3
        for num in nums:
            count[num] += 1
        idx = 0
        
        for i in range(len(nums)):
            if count[idx] == 0:
                idx += 1
            if count[idx] == 0:
                idx += 1
            nums[i] = idx
            count[idx] -= 1
