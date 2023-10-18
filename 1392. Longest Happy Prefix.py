class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0] * len(s)
        prev = 0
        for i in range(1, len(s)):
            while prev != 0 and s[prev] != s[i]:
                prev = LPS[prev-1]
            if s[prev] == s[i]:
                LPS[i] = prev + 1
                prev += 1
        
        return s[:LPS[-1]]
        
