class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            string = str(nums[i])
            num = [*string]
            num.reverse()
            nums.append(int("".join(num)))
        
        return len(set(nums))
