class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ordered = [None]*n
        p_idx = 0
        n_idx = 1

        for num in nums:
            if num > 0:
                ordered[p_idx] = num
                p_idx += 2
            else:
                ordered[n_idx] = num
                n_idx += 2

        return ordered
