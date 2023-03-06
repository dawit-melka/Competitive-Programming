class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, len(nums)

        while right > left + 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        
        if right == len(nums) or nums[right] != target:
            return [-1, -1]
        
        first = right
        left, right = -1, len(nums)
        
        while right > left + 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        
        last = left
        return [first, last]
