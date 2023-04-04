class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise = float("-inf")
        curr_subset = []
        count = 0

        def calculateBitwise(arr):
            curr = 0
            for num in arr:
                curr = curr | num
            
            return curr

        def backtrack(index):
            nonlocal max_bitwise
            nonlocal count

            if index == len(nums):
                curr_bitwise = calculateBitwise(curr_subset)
                if curr_bitwise > max_bitwise:
                    count = 1
                    max_bitwise = curr_bitwise
                elif curr_bitwise == max_bitwise:
                    count += 1
                return
            
            curr_subset.append(nums[index])
            backtrack(index + 1)
            curr_subset.pop()
            backtrack(index + 1)

        backtrack(0)

        return count
