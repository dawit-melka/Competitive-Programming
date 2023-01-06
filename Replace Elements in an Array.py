class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_idexs = {}
        for i, num in enumerate(nums):
            num_idexs[num] = i
        
        for curr_val, new_val in operations:
            idx = num_idexs[curr_val]
            nums[idx] = new_val
            num_idexs[new_val] = idx
            del num_idexs[curr_val]

        return nums
