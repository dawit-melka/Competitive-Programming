class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = len(strs)
        m = len(strs[0])
        first_str = strs[0]
        for i in range(m):
            curr = first_str[i]
            for j in range(1,n):
                if i >= len(strs[j]) or first_str[i] != strs[j][i]:
                    curr = False
                    break
            if curr: res += curr
            else: break

        return res