class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = Counter(p)
        l, r = 0, 0
        result = []
        k = len(p)

        for r in range(len(s)):
            while l < r and not freq_p.get(s[r]):
                freq_p[s[l]] += 1
                l += 1
            if s[r] in freq_p:
                freq_p[s[r]] -= 1
            else:
                l += 1

            if r - l + 1 == k:
                result.append(l)

        return result
