class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largest, smallest = max(nums), min(nums)

        while True:
            remainder = largest % smallest
            if remainder == 0:
                return smallest
            largest = smallest
            smallest = remainder
