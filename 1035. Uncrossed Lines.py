class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}

        def dfs(i1, i2):
            if i1 == len(nums1) or i2 == len(nums2):
                return 0
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            ans = 0
            if nums1[i1] == nums2[i2]:
                ans = max(ans, 1 + dfs(i1 +1, i2 +1), dfs(i1, i2+1), dfs(i1+1, i2))
            else:
                ans = max(dfs(i1, i2+1), dfs(i1+1, i2))
            
            cache[(i1, i2)] = ans 
            return ans
        
        return dfs(0, 0)
