class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [pivot]*(n)
        low_idx = 0
        high_idx = -1

        for i in range(n):
            if nums[i] < pivot:
                result[low_idx] = nums[i]
                low_idx += 1
            if nums[-i-1] > pivot:
                result[high_idx] = nums[-i-1]
                high_idx -= 1

        return result
