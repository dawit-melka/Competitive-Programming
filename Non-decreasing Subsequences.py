class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        result = []
        curr = []
        
        def backtrack(idx):
            if len(curr) >= 2 and tuple(curr) not in seen:
                result.append(curr.copy())
                seen.add(tuple(curr))
            if idx >= len(nums): return

            if not curr or curr[-1] <= nums[idx]:
                curr.append(nums[idx])
                backtrack(idx + 1)
                curr.pop()
            backtrack(idx + 1)

        backtrack(0)
        return result
