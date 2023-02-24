class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2

        left = 0
        result = 0
        window_sum = 0
        back_zeros = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            
            while window_sum > k:
                back_zeros = 0
                window_sum -= nums[left]
                left += 1
            
            if window_sum == k:
                while nums[left] == 0:
                    back_zeros += 1
                    left += 1
                result += back_zeros + 1

        return result
