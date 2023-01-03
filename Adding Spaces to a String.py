class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        res = []
        n = len(s)
        for i in range(n):
            if i in spaces:
                res.append(" ")
            res.append(s[i])

        return "".join(res)
