class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(curr, idx):
            subsets.append(curr.copy())
            if idx >= len(nums):
                return

            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()

        backtrack([], 0)

        return subsets
