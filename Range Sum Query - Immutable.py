class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i-1]
        self.nums.append(0)
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - self.nums[left-1]
