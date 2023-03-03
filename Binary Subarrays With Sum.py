class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = Counter()
        freq[0] = 1

        count = 0
        runnSum = 0

        for i in range(len(nums)):
            runnSum += nums[i]

            if (runnSum - goal) in freq:
                count += freq[runnSum - goal]
            freq[runnSum] += 1

        return count
