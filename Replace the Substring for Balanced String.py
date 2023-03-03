class Solution:
    def balancedString(self, s: str) -> int:
        freq = Counter(s)
        n = len(s)//4

        for char in ["Q", "W", "E", "R"]:
            freq[char] = freq[char] - n

        def isBalanced(dict_):
            for char in dict_:
                if dict_[char] > 0:
                    return False
            return True

        left, right = 0, 0
        res = len(s)
        while right < len(s):
            while right < len(s) and not isBalanced(freq):
                freq[s[right]] -= 1
                right += 1

            while left < len(s) and isBalanced(freq):
                res = min(res, right - left)
                freq[s[left]] += 1
                left += 1
            
        return res
