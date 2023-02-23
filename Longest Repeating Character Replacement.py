class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = [0]*26
        left = 0
        result = 0

        for right in range(len(s)):
            char_freq[ord(s[right]) - ord("A")] += 1
            while sum(char_freq) - max(char_freq) > k:
                char_freq[ord(s[left]) - ord("A")] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
