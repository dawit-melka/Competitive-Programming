class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        size = len(s)
        max_len = 0
        left = 0

        for right in range(size):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            unique_chars.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
