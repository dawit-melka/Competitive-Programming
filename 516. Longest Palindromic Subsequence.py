class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}

        def LPS(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left > right:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                memo[(left, right)] = 2 + LPS(left+1, right-1)
                return memo[(left, right)]
            else:
                memo[(left, right)] = max(LPS(left, right-1), LPS(left+1, right))
                return memo[(left, right)]

        return LPS(0, n-1)
