class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        result = 0
        for num in nums:
            if (k - num) in count and count[k-num] > 0:
                result += 1
                count[k-num] -= 1
            else:
                count[num] += 1
        return result
