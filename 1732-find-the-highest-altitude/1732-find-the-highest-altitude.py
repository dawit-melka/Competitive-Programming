class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        running_sum = 0
        
        for num in gain:
            running_sum += num
            result = max(result, running_sum)
        
        return result