class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float("inf")

        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        
        return False
