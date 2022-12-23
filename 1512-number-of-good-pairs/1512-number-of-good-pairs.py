class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        ans = 0

        for val in nums:
            if val in freq:
                ans += freq[val]
                freq[val] += 1
            else:
                freq[val] = 1
        
        return ans