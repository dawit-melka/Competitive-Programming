class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = Counter(s1)
        l, r = 0, 0
        k = len(s1)

        for r in range(len(s2)):
            while l < r and not freq_s1.get(s2[r]):
                freq_s1[s2[l]] += 1
                l += 1
            if s2[r] in freq_s1:
                freq_s1[s2[r]] -= 1
            else:
                l += 1
            if r - l + 1 == k:
                return True

        return False
