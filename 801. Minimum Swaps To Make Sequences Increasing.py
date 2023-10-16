class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}
        def dp(i, prev_n1, prev_n2):
            if i == len(nums2):
                return 0
            if (i, prev_n1, prev_n2) in cache:
                return cache[(i, prev_n1, prev_n2)]
            if nums1[i] > prev_n1 and nums2[i] > prev_n2 and nums1[i] > prev_n2 and nums2[i] > prev_n1:
                cache[(i, prev_n1, prev_n2)] = min(1 + dp(i+1, nums2[i], nums1[i]), dp(i+1, nums1[i], nums2[i]))
            elif nums1[i] > prev_n1 and nums2[i] > prev_n2:
                cache[(i, prev_n1, prev_n2)] = dp(i+1, nums1[i], nums2[i])
            elif nums1[i] > prev_n2 and nums2[i] > prev_n1:
                cache[(i, prev_n1, prev_n2)] = 1 + dp(i+1, nums2[i], nums1[i])
            else:
                cache[(i, prev_n1, prev_n2)] = float("inf")
            return cache[(i, prev_n1, prev_n2)]
        
        return dp(0, float("-inf"), float("-inf"))


        
